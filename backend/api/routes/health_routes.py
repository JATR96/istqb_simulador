from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Endpoint simple de salud.
    """

    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }


@router.get("/db")
def database_check(db: Session = Depends(get_db)):
    """
    Verifica conexión con MySQL.
    """

    db.execute(text("SELECT 1"))

    return {
        "database": "connected"
    }