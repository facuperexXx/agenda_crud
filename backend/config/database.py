from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
DATABASE_URL = os.path.join(BASE_DIR, "agenda.db")

engine = create_engine("sqlite:////" + DATABASE_URL)

# Configuración de conexion a la base de datos 
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Inicializa la base de datos
def init_db():
    from models import Contacto
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada!")