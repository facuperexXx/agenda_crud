from flask import Flask
from config import get_db
from models import ContactoSchema, Contacto, APIResponse

def probar_db():
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
        print(resultado)
        print(type(resultado))

        jason = schema.dump(resultado)
        print(jason)

        db.add(resultado)
        db.commit()

    except Exception as e:
        print(e.messages)

app = Flask(__name__)

@app.route('/')
def home():
    probar_db()
    return "API en funcionamiento"

# endpoint - obtener todos los registros
@app.route('/contactos')
def all_contactos():
    try:
        schema = ContactoSchema()

        # Variables de respuesta
        lista_final = []
        count = 0
        message = "Peticion ejecutada"

        # Obtener los registros de la base de datos
        registros = db.query(Contacto).all()

        # Recopilando registros
        for r in registros:

            # Convierte los registros sacados de la consulta en una lista de diccionarios
            lista_final.append(schema.dump(r))
            count += 1

        # Generando respuesta
        respuesta = APIResponse(True, lista_final, count, message)

        return respuesta.to_json()
    
    except:
        return APIResponse(False, [], 0, "Peticion rechazada").to_json()

# endpoint - buscar registro con id
@app.route('/buscar/<int:id>')
def buscarXid(id):
    try:
        schema = ContactoSchema()
        id_buscado = id

        # Variables de respuesta
        lista_final = []
        count = 0
        message = "Peticion ejecutada"

        # ejecucion de consulta
        registro_buscado = db.get(Contacto, id_buscado)

        if registro_buscado:
            lista_final.append(schema.dump(registro_buscado))

            count = len(lista_final)

        else:
            # en caso de no encontrar registro
            message = "Registro no encontrado"

        # generacion de la respuesta
        respuesta = APIResponse(True, lista_final, count, message)
        return respuesta.to_json()

    except:
        return APIResponse(False, [], 0, "Peticion rechazada").to_json()



# ejecucion de API
if __name__ == '__main__':
    db = get_db()
    app.run(debug=True, port=8040)
