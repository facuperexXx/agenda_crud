from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///agenda.db"

engine = create_engine(DATABASE_URL)

# Configuración de conexion a la base de datos 
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Inicializa la base de datos
def init_db():
    from models import Contacto
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada!")