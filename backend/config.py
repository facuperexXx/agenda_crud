from database import init_db, engine, SessionLocal

def get_db():
    # Se inicializa la base de datos | si no existe, la crea
    init_db()

    # Instancia de la base de datos 
    return SessionLocal()