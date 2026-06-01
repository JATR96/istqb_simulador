from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()


class Settings:
    """
    Configuración global del proyecto.
    """

    DATABASE_URL: str = os.getenv("DATABASE_URL")


# Instancia global
settings = Settings()