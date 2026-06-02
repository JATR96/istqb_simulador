from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from services.import_service import import_questions

router = APIRouter(
    prefix="/import",
    tags=["Import"]
)


@router.post("/foundation")
def import_foundation_questions(
    db: Session = Depends(get_db)
):
    """
    Importar preguntas Foundation.
    """

    result = import_questions(
        db=db,
        json_path="data/foundation/foundation_questions.json"
    )

    return result