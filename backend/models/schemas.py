from marshmallow import Schema, fields, post_load
from models import Contacto

class ContactoSchema(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    direccion = fields.Str(required=True)
    email = fields.Email(required=True)
    telefono = fields.Str(required=True)

    @post_load
    def generar_contacto(self, data, **kwargs):
        return Contacto(**data)
    