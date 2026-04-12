from database import Base
from sqlalchemy import Column, Integer, String

class Contacto(Base):
    __tablename__ = "contactos"

    id = Column(Integer(), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    email = Column(String)
    telefono = Column(String)
