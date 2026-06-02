from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.result_schema import (
    SubmitExamRequest,
    SubmitExamResponse
)

from services.result_service import (
    process_exam_result
)

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


# ==========================================
# SUBMIT EXAM
# ==========================================

@router.post(
    "/submit",
    response_model=SubmitExamResponse
)
def submit_exam(
    request: SubmitExamRequest,
    db: Session = Depends(get_db)
):
    """
    Procesa examen y genera score.
    """

    return process_exam_result(
        db=db,
        request=request
    )