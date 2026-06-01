from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

"""
Configuración principal de SQLAlchemy.

Aquí se define:
- conexión MySQL
- engine
- sesiones
- Base declarativa
"""

# Crear engine de conexión
engine = create_engine(
    settings.DATABASE_URL,
    echo=True  # Mostrar SQL en consola
)

# Crear sesión local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos ORM
Base = declarative_base()


def get_db():
    """
    Dependency Injection para FastAPI.

    Proporciona una sesión de base de datos
    y la cierra automáticamente.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()