from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from models.question_model import Question

from schemas.question_schema import QuestionResponse

from typing import List

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


# ==========================================
# OBTENER TODAS LAS PREGUNTAS
# ==========================================

@router.get(
    "/",
    response_model=List[QuestionResponse]
)
def get_questions(
    db: Session = Depends(get_db)
):
    """
    Retorna todas las preguntas.
    """

    questions = db.query(Question).all()

    return questions