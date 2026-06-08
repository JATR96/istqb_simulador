from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.exam_schema import (
    GenerateExamRequest,
    GenerateExamResponse
)

from services.exam_service import (
    generate_quick_exam,
    generate_chapter_exam,
    generate_lo_exam,
    generate_official_exam
)

router = APIRouter(
    prefix="/exams",
    tags=["Exams"]
)


# ==========================================
# GENERAR EXAMEN
# ==========================================

@router.post(
    "/generate",
    response_model=GenerateExamResponse
)
def generate_exam(
    request: GenerateExamRequest,
    db: Session = Depends(get_db)
):
    """
    Generador principal de exámenes.
    """

    print("================================")
    print("CERTIFICATION:", request.certification)
    print("LANGUAGE:", request.language)
    print("EXAM MODE:", request.exam_mode)
    print("QUESTION COUNT:", request.question_count)
    print("================================")

    # ======================================
    # QUICK EXAM
    # ======================================

    if request.exam_mode == "quick":

        return generate_quick_exam(
            db=db,

            certification=
                request.certification,

            language=
                request.language,

            question_count=
                request.question_count
        )

    # ======================================
    # CHAPTER EXAM
    # ======================================

    if request.exam_mode == "chapter":

        return generate_chapter_exam(
            db=db,

            certification=
                request.certification,

            language=
                request.language,

            chapters=
                request.chapters,

            question_count=
                request.question_count
        )

    # ======================================
    # LEARNING OBJECTIVE EXAM
    # ======================================

    if request.exam_mode == "learning_objective":

        return generate_lo_exam(
            db=db,

            certification=
                request.certification,

            language=
                request.language,

            learning_objectives=
                request.learning_objectives,

            question_count=
                request.question_count
        )

    # ======================================
    # OFFICIAL EXAM
    # ======================================

    if request.exam_mode == "official":

        return generate_official_exam(
            db=db,

            certification=
                request.certification,

            language=
                request.language
        )

    return {
        "total_questions": 0,
        "requested_questions": 0,
        "adjusted": False,
        "questions": []
    }