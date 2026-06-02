from sqlalchemy.orm import Session

from models.question_model import Question

from models.exam_attempt_model import (
    ExamAttempt
)

from models.user_answer_model import (
    UserAnswer
)

"""
Servicio profesional de resultados.
"""


# ==========================================
# PROCESAR EXAMEN
# ==========================================

def process_exam_result(
    db: Session,
    request
):
    """
    Procesa respuestas y calcula score.
    """

    correct_answers = 0

    review = []

    # ======================================
    # CREAR EXAM ATTEMPT
    # ======================================

    exam_attempt = ExamAttempt(

        certification=
            request.certification,

        exam_mode=
            request.exam_mode,

        language=
            request.language,

        total_questions=
            len(request.answers),

        correct_answers=0,

        incorrect_answers=0,

        score=0,

        passed=False,

        duration_seconds=
            request.duration_seconds
    )

    db.add(exam_attempt)

    db.flush()

    # ======================================
    # VALIDAR RESPUESTAS
    # ======================================

    for answer in request.answers:

        question = db.query(
            Question
        ).filter(
            Question.id ==
            answer.question_id
        ).first()

        translation = question.translations[
            request.language
        ]

        correct_option_id = translation[
            "respuesta_correcta_id"
        ]

        is_correct = (
            answer.selected_option_id ==
            correct_option_id
        )

        if is_correct:
            correct_answers += 1

        # ==================================
        # GUARDAR USER ANSWER
        # ==================================

        user_answer = UserAnswer(

            exam_attempt_id=
                exam_attempt.id,

            question_id=
                question.id,

            selected_option_id=
                answer.selected_option_id,

            is_correct=is_correct
        )

        db.add(user_answer)

        # ==================================
        # REVIEW
        # ==================================

        review.append({

            "question_id":
                question.id,

            "question":
                translation[
                    "pregunta"
                ],

            "selected_option_id":
                answer.selected_option_id,

            "correct_option_id":
                correct_option_id,

            "is_correct":
                is_correct,

            "explanation":
                translation[
                    "explicacion"
                ]
        })

    # ======================================
    # SCORE
    # ======================================

    total_questions = len(
        request.answers
    )

    incorrect_answers = (
        total_questions -
        correct_answers
    )

    score = round(
        (
            correct_answers /
            total_questions
        ) * 100,
        2
    )

    # ======================================
    # ISTQB PASS SCORE
    # ======================================

    passed = score >= 65

    # ======================================
    # UPDATE ATTEMPT
    # ======================================

    exam_attempt.correct_answers = (
        correct_answers
    )

    exam_attempt.incorrect_answers = (
        incorrect_answers
    )

    exam_attempt.score = score

    exam_attempt.passed = passed

    db.commit()

    return {

        "score": score,

        "passed": passed,

        "total_questions":
            total_questions,

        "correct_answers":
            correct_answers,

        "incorrect_answers":
            incorrect_answers,

        "review": review
    }