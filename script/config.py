import os

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")  # URI de la base de datos
DATABASE = os.environ.get("DATABASE", "adtr_ufte")  # Nombre de la base de datos
COLLECTION = os.environ.get("COLLECTION", "usuarios")  # Nombre de la colección
SECRET_KEY = os.environ.get("SECRET_KEY", "tu_clave_secreta")  # Clave secreta para la sesión
SQLALCHEMY_DATABASE_URI = "postgresql://usuario:3000Leonidas@localhost:5432/nombre_db"

