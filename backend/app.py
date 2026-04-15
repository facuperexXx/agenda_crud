from flask import Flask, request
from config import get_db
from models import ContactoSchema, Contacto, APIResponse

def buscar_registro(id_buscado):
        # ejecucion de consulta
        registro_buscado = db.query(Contacto).filter_by(id = id_buscado).first()

        return registro_buscado

app = Flask(__name__)

@app.route('/')
def home():
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
def buscar_por_id(id):
    try:
        schema = ContactoSchema()
        id_buscado = id

        # Variables de respuesta
        lista_final = []
        count = 0
        message = "Peticion ejecutada"

        registro_buscado = buscar_registro(id_buscado)

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

@app.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_por_id(id):
    try:
        id_buscado = id

        # Variables de respuesta
        lista_final = []
        count = 0
        message = "Peticion ejecutada"

        # busqueda y eliminacion del registro
        if buscar_registro(id):
            registro_a_eliminar = buscar_registro(id)
            db.delete(registro_a_eliminar)
            db.commit()
        
        else:
            # en caso de no haber registro por eliminar
            message = f"Registro {id_buscado} no encontrado"

        # generacion de la respuesta
        respuesta = APIResponse(True, lista_final, count, message)
        return respuesta.to_json()

    except:
        return APIResponse(False, [], 0, "Peticion rechazada").to_json()
    
@app.route('/nuevo', methods=['POST'])   
def crear_registro():
    try:
        schema = ContactoSchema()

        # Variables de respuesta
        lista_final = []
        count = 0
        message = "Peticion ejecutada"

        # obtencion de datos recibidos
        datos = request.get_json()

        # vericacion y creacion de registro
        nuevo_registro = schema.load(datos)

        # guardado en base de datos
        db.add(nuevo_registro)
        db.commit()

        # verificacion de registro guardado 
        id_registro = nuevo_registro.id

        if id_registro:    
            registro = buscar_registro(id_registro)

            lista_final.append(schema.dump(registro))
            count = len(lista_final)

            # informo id del registro cargado
            message += f" - Registro {id_registro}"

        # generacion de respuesta
        respuesta = APIResponse(True, lista_final, count, message)

        return respuesta.to_json()
    
    except:
        return APIResponse(False, [], 0, "Peticion rechazada").to_json()

@app.route('/modificar/<int:id>', methods=['POST'])
def modificar_registro(id):
    try:
        id_buscado = id
        schema = ContactoSchema()
        datos_actualizacion = request.get_json()

        # busqueda de registro 
        registro = buscar_registro(id_buscado)

        # actualizacion de campos del atributo buscado
        if registro:
            for key, valor in datos_actualizacion.items():
                if hasattr(registro, key):  # el registro tiene un atributo con ese nombre ?
                    setattr(registro, key, valor)   # entonces actualiza el registro con los datos que se envian

            db.commit()     # guardado de cambios

        return buscar_por_id(id_buscado)    # llamado a otro endpoint - funcional pero no recomendable

    except:
        return APIResponse(False, [], 0, "Peticion rechazada").to_json()

# ejecucion de API
if __name__ == '__main__':
    db = get_db()
    app.run(debug=True, port=8040)
