import os
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from datetime import datetime
import traceback
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de CORS para permitir solicitudes desde el frontend
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

bcrypt = Bcrypt(app)

# Configuración de la clave secreta para la sesión
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app) # Un-comment this line.
Session(app)

# Modelos de la base de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float)
    humedad = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Decorador para proteger rutas (con roles)
def login_required(roles=None):
    def decorator(f):
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'message': 'Acceso no autorizado'}), 401

            if roles is not None and not callable(roles): # Added this check
                user = User.query.filter_by(id=session.get('user_id')).first()
                if user and user.role not in roles:
                    return jsonify({'message': 'Acceso no autorizado (rol incorrecto)'}), 403

            return f(*args, **kwargs)
        decorated_function.__name__ = f.__name__
        decorated_function.__doc__ = f.__doc__
        return decorated_function
    if callable(roles):
        return decorator(roles)
    return decorator

# Ruta para registrar usuarios
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role')

    if not username or not password or not email:
        return jsonify({'message': 'Faltan datos'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'El usuario ya existe'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        if role: # Si el rol fue proporcionado
            new_user = User(username=username, hashed_password=hashed_password, email=email, role=role)
        else: # Si el rol no fue proporcionado, usa el rol por defecto.
            new_user = User(username=username, hashed_password=hashed_password, email=email, role='user')
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Usuario registrado'}), 201

    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return jsonify({'message': 'Error al registrar usuario'}), 500
    

# Ruta para iniciar sesión
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.hashed_password, password):
        session['user_id'] = user.id
        response = jsonify({'message': 'Inicio de sesión exitoso', 'role': user.role, 'username': user.username})
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

# Ruta para cerrar sesión
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Sesión cerrada exitosamente'}), 200

# Ruta protegida (ejemplo)
@app.route('/api/protected', methods=['GET'])
@login_required
def protected_route():
    user = User.query.filter_by(id=session.get('user_id')).first()
    if user:
        return jsonify({'message': 'Ruta protegida', 'user_data': {'username': user.username}})
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

# Ruta para obtener la lista de usuarios (solo para administradores)
@app.route('/api/users', methods=['GET'])
@login_required(roles=['admin'])
def get_users():
    try:
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'role': user.role} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': 'Error al obtener usuarios'}), 500

# Ruta para testear la base de datos
@app.route('/api/test_db', methods=['GET'])
def test_db():
    try:
        db.session.query(SensorData).first()
        return jsonify({'message': 'Conexión a la base de datos exitosa'}), 200
    except Exception as e:
        return jsonify({'message': f'Error de conexión a la base de datos: {str(e)}'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Crea las tablas en la base de datos
    app.run(debug=True)