from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from services.import_all_questions import (
    import_all_questions
)

router = APIRouter(
    prefix="/import",
    tags=["Import"]
)


@router.post("/all")
def import_all(
    db: Session = Depends(get_db)
):
    """
    Importa todas las preguntas
    encontradas en data/.
    """

    result = import_all_questions(
        db=db,
        data_directory="data"
    )

    return result