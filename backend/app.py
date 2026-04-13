from database import init_db, engine

from sqlalchemy import inspect

init_db()

inspector = inspect(engine)

tablas = inspector.get_table_names()

if "contactos" in tablas:
    print("La tabla existe.")
else:
    print("No hay tabla.")

from models import ContactoSchema

data_externa = {
    "nombre" : "Mambo",
    "apellido" : "Perez",
    "direccion" : "Franklin",
    "email" : "mambito@gmail.com",
    "telefono" : "444-222"
}

schema = ContactoSchema()

try:
    resultado = schema.load(data_externa)
    print(type(resultado))

    jason = schema.dump(resultado)
    print(jason)

except Exception as e:
     print(e.messages)