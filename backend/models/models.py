from config import Base
from sqlalchemy import Column, Integer, String

class Contacto(Base):
    __tablename__ = "contactos"

    id = Column(Integer(), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    email = Column(String)
    telefono = Column(String)

    def to_dict(self):
        return {"id" : self.id, "nombre" : self.nombre, "apellido" : self.apellido, "direccion" : self.direccion, "email" : self.email, "telefono" : self.telefono}
