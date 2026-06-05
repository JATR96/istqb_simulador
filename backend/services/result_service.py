from sqlalchemy.orm import Session

from models.question_model import Question

from models.exam_attempt_model import (
    ExamAttempt
)

from models.user_answer_model import (
    UserAnswer
)

from services.certification_service import (
    load_certification_config
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

    total_points = 0

    earned_points = 0

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

        question = (
            db.query(Question)
            .filter(
                Question.id ==
                answer.question_id
            )
            .first()
        )

        if not question:
            continue

        translation = (
            question.translations[
                request.language
            ]
        )

        # ==================================
        # DATOS DE PREGUNTA
        # ==================================

        correct_option_ids = (
            question.respuestas_correctas
        )

        question_type = (
            question.tipo_pregunta
        )

        question_points = (
            question.points
        )

        total_points += question_points

        # ==================================
        # VALIDAR RESPUESTA
        # ==================================

        is_correct = False

        if question_type == "eleccion_simple":

            is_correct = (

                len(answer.selected_option_ids) > 0

                and

                answer.selected_option_ids[0]
                ==
                correct_option_ids[0]

            )

        elif question_type == "eleccion_multiple":

            selected_answers = set(
                answer.selected_option_ids
            )

            expected_answers = set(
                correct_option_ids
            )

            is_correct = (
                selected_answers ==
                expected_answers
            )

        # ==================================
        # CONTABILIZAR SCORE
        # ==================================

        if is_correct:

            correct_answers += 1

            earned_points += question_points

        # ==================================
        # GUARDAR USER ANSWER
        # ==================================

        user_answer = UserAnswer(

            exam_attempt_id=
                exam_attempt.id,

            question_id=
                question.id,

            selected_option_ids=
                answer.selected_option_ids,

            is_correct=
                is_correct
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

            "options":
                translation[
                    "opciones"
                ],

            "selected_option_ids":
                answer.selected_option_ids,

            "correct_option_ids":
                correct_option_ids,

            "is_correct":
                is_correct,

            "type":
                question.tipo_pregunta,

            "k_level":
                question.k_level,

            "points":
                question.points,

            "certification":
                question.certification,

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

    if total_points > 0:

        score = round(

            (
                earned_points /
                total_points
            ) * 100,

            2
        )

    else:

        score = 0

    # ======================================
    # CERTIFICACIÓN
    # ======================================

    config = load_certification_config(
        request.certification
    )

    passing_points = config[
        "passing_points"
    ]

    passed = (
        earned_points >=
        passing_points
    )

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

    # ======================================
    # RESPONSE
    # ======================================

    return {

        "score":
            score,

        "earned_points":
            earned_points,

        "total_points":
            total_points,

        "passing_points":
            passing_points,

        "passed":
            passed,

        "total_questions":
            total_questions,

        "correct_answers":
            correct_answers,

        "incorrect_answers":
            incorrect_answers,

        "review":
            review
    }