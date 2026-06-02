from sqlalchemy.orm import Session

from sqlalchemy import func

from models.exam_attempt_model import (
    ExamAttempt
)

from models.user_answer_model import (
    UserAnswer
)

"""
Servicio profesional de estadísticas.
"""


# ==========================================
# OBTENER ESTADÍSTICAS
# ==========================================

def get_global_statistics(
    db: Session
):
    """
    Obtiene estadísticas globales.
    """

    # ======================================
    # TOTAL EXAMS
    # ======================================

    total_exams = db.query(
        ExamAttempt
    ).count()

    # ======================================
    # AVERAGE SCORE
    # ======================================

    average_score = db.query(
        func.avg(
            ExamAttempt.score
        )
    ).scalar()

    if average_score is None:
        average_score = 0

    average_score = round(
        average_score,
        2
    )

    # ======================================
    # PASSED / FAILED
    # ======================================

    passed_exams = db.query(
        ExamAttempt
    ).filter(
        ExamAttempt.passed == True
    ).count()

    failed_exams = db.query(
        ExamAttempt
    ).filter(
        ExamAttempt.passed == False
    ).count()

    # ======================================
    # PASS RATE
    # ======================================

    if total_exams == 0:
        pass_rate = 0

    else:

        pass_rate = round(
            (
                passed_exams /
                total_exams
            ) * 100,
            2
        )

    # ======================================
    # SCORE HISTORY
    # ======================================

    history = db.query(
        ExamAttempt
    ).order_by(
        ExamAttempt.created_at.desc()
    ).all()

    score_history = []

    for item in history:

        score_history.append({

            "id": item.id,

            "certification":
                item.certification,

            "score":
                item.score,

            "passed":
                item.passed,

            "created_at":
                item.created_at.isoformat()
        })

    # ======================================
    # MOST INCORRECT QUESTIONS
    # ======================================

    incorrect_questions_query = db.query(

        UserAnswer.question_id,

        func.count(
            UserAnswer.question_id
        ).label(
            "incorrect_count"
        )

    ).filter(

        UserAnswer.is_correct == False

    ).group_by(

        UserAnswer.question_id

    ).order_by(

        func.count(
            UserAnswer.question_id
        ).desc()

    ).limit(10).all()

    incorrect_questions = []

    for item in incorrect_questions_query:

        incorrect_questions.append({

            "question_id":
                item.question_id,

            "incorrect_count":
                item.incorrect_count
        })

    return {

        "total_exams":
            total_exams,

        "average_score":
            average_score,

        "passed_exams":
            passed_exams,

        "failed_exams":
            failed_exams,

        "pass_rate":
            pass_rate,

        "score_history":
            score_history,

        "incorrect_questions":
            incorrect_questions
    }