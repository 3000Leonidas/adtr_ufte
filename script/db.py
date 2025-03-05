from pymongo import MongoClient
from .config import MONGO_URI, DATABASE, COLLECTION


client = MongoClient(MONGO_URI)
db = client[DATABASE]
collection = db[COLLECTION]


def connect_db():
    try:
        # Verificar la conexión (opcional)
        client.admin.command('ping')
        print("Conexión a MongoDB exitosa")
        return collection
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        return None