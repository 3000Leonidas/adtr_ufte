from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
from script.db import connect_db
from functools import wraps
from bson.objectid import ObjectId
import traceback
import os


app = Flask(__name__)

# Configuración de CORS para permitir solicitudes desde el frontend
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

bcrypt = Bcrypt(app)

# Configuración de la clave secreta para la sesión
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Conexión a la base de datos
collection = connect_db()  # Asegúrate de que la conexión a la base de datos se realiza correctamente
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# Decorador para proteger rutas (con roles)
def login_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'message': 'Acceso no autorizado'}), 401

            if roles is not None:  # Verifica si se especificaron roles
                user_id_str = session.get('user_id')
                user_id = ObjectId(user_id_str)
                user = collection.find_one({'_id': user_id})
                if user and user.get('role') not in roles:  # Verifica si el rol del usuario está permitido
                    return jsonify({'message': 'Acceso no autorizado (rol incorrecto)'}), 403

            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Ruta para registrar usuarios
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')  # Obtén el email del cuerpo de la solicitud

    if not username or not password or not email:  # Verifica si faltan datos
        return jsonify({'message': 'Faltan datos'}), 400

    existing_user = collection.find_one({'username': username})
    if existing_user:
        return jsonify({'message': 'El usuario ya existe'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        new_user = {
            'username': username,
            'hashed_password': hashed_password,
            'email': email,  # Guarda el email en la base de datos
            'role': 'user'  # Asigna el rol "user" por defecto
        }

        collection.insert_one(new_user)

        return jsonify({'message': 'Usuario registrado'}), 201  # Respuesta sin iniciar sesión

    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return jsonify({'message': 'Error al registrar usuario'}), 500

# Ruta para iniciar sesión
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = collection.find_one({'username': username})

    if user and bcrypt.check_password_hash(user['hashed_password'], password):
        session['user_id'] = str(user['_id'])
        role = user['role']  # Obtén el rol del usuario
        response = jsonify({'message': 'Inicio de sesión exitoso', 'role': role, 'username': username})  # Incluye el rol y el username en la respuesta
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
    user_id_str = session.get('user_id')
    if user_id_str:
        try:
            user_id = ObjectId(user_id_str)
            user = collection.find_one({'_id': user_id})

            if user:
                return jsonify({'message': 'Ruta protegida', 'user_data': {'username': user['username']}})
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404

        except Exception as e:
            print(f"Error en protected: {e}")
            return jsonify({'message': 'Error al acceder a datos'}), 500

    else:
        return jsonify({'message': 'No has iniciado sesión'}), 401

# Ruta para obtener la lista de usuarios (solo para administradores)
@app.route('/api/users', methods=['GET'])
@login_required(roles=['admin'])
def get_users():
    try:
        users = list(collection.find({}, {"_id": 0}))
        return jsonify(users), 200
    except Exception as e:
        traceback.print_exc()  # Imprime el traceback completo en la consola
        return jsonify({'message': 'Error al obtener usuarios'}), 500

if __name__ == '__main__':
    app.run(debug=True)

else:
    print("Error al conectar a la base de datos")
    exit()