from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Modelo para datos de sensores
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=False)
    humedad = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Ruta para recibir datos de sensores
@app.route('/api/sensores', methods=['POST'])
def guardar_sensores():
    data = request.get_json()
    temperatura = data.get('temperatura')
    humedad = data.get('humedad')

    if temperatura is None or humedad is None:
        return jsonify({'message': 'Faltan datos'}), 400

    nuevo_dato = SensorData(temperatura=temperatura, humedad=humedad)
    db.session.add(nuevo_dato)
    db.session.commit()

    return jsonify({'message': 'Datos guardados correctamente'}), 201

# Ruta para obtener los datos de sensores
@app.route('/api/sensores', methods=['GET'])
def obtener_sensores():
    datos = SensorData.query.order_by(SensorData.timestamp.desc()).limit(10).all()
    resultado = [
        {"temperatura": d.temperatura, "humedad": d.humedad, "timestamp": d.timestamp}
        for d in datos
    ]
    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
