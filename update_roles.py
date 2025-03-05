import os
from pymongo import MongoClient

# Obtén las variables de entorno
uri = os.environ.get("MONGODB_URI")
db_name = os.environ.get("MONGODB_DB_NAME")
collection_name = "usuarios"  # Nombre *exacto* de la colección (¡verifícalo en MongoDB Compass!)

print(f"URI: {uri}")
print(f"Base de datos: {db_name}")
print(f"Colección: {collection_name}")

if not all([uri, db_name]):
    print("Error: Faltan variables de entorno (MONGODB_URI o MONGODB_DB_NAME).")
    exit()

try:
    client = MongoClient(uri)
    db = client[db_name]

    print(f"Colecciones disponibles en la base de datos '{db_name}': {db.list_collection_names()}")  # Comprobación

    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        print(f"Colección '{collection_name}' encontrada. Procediendo con la actualización...")

        try:
            result = collection.update_many(
                {'role': {'$exists': False}},
                {'$set': {'role': 'user'}}
            )
            print(f"Se actualizaron {result.modified_count} usuarios.")

            for user in collection.find({'role': 'user'}):
                print(user)

        except Exception as e:
            print(f"Error al actualizar o leer documentos: {e}")
            import traceback
            traceback.print_exc()

    else:
        print(f"La colección '{collection_name}' no existe.  Revisa *cuidadosamente* el nombre en MongoDB Compass.")
        # Aquí puedes añadir código para crear la colección si lo deseas (como se explicó antes)

except Exception as e:
    print(f"Error de conexión o acceso a la base de datos: {e}")
    import traceback
    traceback.print_exc()

finally:
    if client:
        client.close()
        print("Conexión cerrada.")