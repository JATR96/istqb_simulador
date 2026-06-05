import random
import json

from sqlalchemy.orm import Session

from models.question_model import Question

"""
Servicio profesional de generación de exámenes.
"""


# ==========================================
# MEZCLAR OPCIONES
# ==========================================

def shuffle_options(options):
    """
    Mezcla dinámicamente las opciones.
    """

    shuffled = options.copy()

    random.shuffle(shuffled)

    return shuffled


# ==========================================
# SERIALIZAR PREGUNTA
# ==========================================

def serialize_question(
    question,
    language
):
    """
    Serializa pregunta según idioma.
    """

    translation = question.translations[
        language
    ]

    options = translation["opciones"]

    shuffled_options = shuffle_options(
        options
    )

    return {
        "id": 
            question.id,

        "type":
            question.tipo_pregunta,

        "k_level":
            question.k_level,

        "points":
            question.points,

        "question": 
            translation[
                "pregunta"
            ],

        "options": 
            shuffled_options,

        "image_url": 
            question.image_url,

        "image_description":
            question.image_description,

        "chapter": 
            question.chapter,

        "section": 
            question.section,

        "learning_objective":
            question.learning_objective
    }


# ==========================================
# EXAMEN RÁPIDO
# ==========================================

def generate_quick_exam(
    db: Session,
    certification: str,
    language: str,
    question_count: int
):
    """
    Genera examen rápido aleatorio.
    """

    questions = db.query(Question).filter(
        Question.certification ==
        certification
    ).all()

    available_questions = len(questions)

    adjusted = False

    # ======================================
    # VALIDAR DISPONIBILIDAD
    # ======================================

    if question_count > available_questions:

        question_count = available_questions

        adjusted = True

    # ======================================
    # RANDOM QUESTIONS
    # ======================================

    selected_questions = random.sample(
        questions,
        question_count
    )

    serialized_questions = [

        serialize_question(
            question,
            language
        )

        for question in selected_questions
    ]

    return {
        "total_questions":
            len(serialized_questions),

        "requested_questions":
            question_count,

        "adjusted":
            adjusted,

        "questions":
            serialized_questions
    }


# ==========================================
# EXAMEN POR CAPÍTULO
# ==========================================

def generate_chapter_exam(
    db: Session,
    certification: str,
    language: str,
    chapters,
    question_count
):
    """
    Genera examen por capítulos.
    """

    questions = db.query(Question).filter(
        Question.certification ==
        certification,

        Question.chapter.in_(chapters)
    ).all()

    available_questions = len(questions)

    adjusted = False

    if question_count > available_questions:

        question_count = available_questions

        adjusted = True

    selected_questions = random.sample(
        questions,
        question_count
    )

    serialized_questions = [

        serialize_question(
            question,
            language
        )

        for question in selected_questions
    ]

    return {
        "total_questions":
            len(serialized_questions),

        "requested_questions":
            question_count,

        "adjusted":
            adjusted,

        "questions":
            serialized_questions
    }


# ==========================================
# EXAMEN LEARNING OBJECTIVES
# ==========================================

def generate_lo_exam(
    db: Session,
    certification: str,
    language: str,
    learning_objectives,
    question_count
):
    """
    Genera examen por learning objectives.
    """

    questions = db.query(Question).filter(
        Question.certification ==
        certification,

        Question.learning_objective.in_(
            learning_objectives
        )
    ).all()

    available_questions = len(questions)

    adjusted = False

    if question_count > available_questions:

        question_count = available_questions

        adjusted = True

    selected_questions = random.sample(
        questions,
        question_count
    )

    serialized_questions = [

        serialize_question(
            question,
            language
        )

        for question in selected_questions
    ]

    return {
        "total_questions":
            len(serialized_questions),

        "requested_questions":
            question_count,

        "adjusted":
            adjusted,

        "questions":
            serialized_questions
    }


# ==========================================
# CARGAR BLUEPRINT
# ==========================================

def load_blueprint(
    certification
):
    """
    Carga blueprint según certificación.
    """

    blueprints = {

        "Foundation Tester":
            "exam_blueprints/foundation_distribution.json",

        "Automation Tester":
            "exam_blueprints/automation_distribution.json"
    }

    blueprint_file = blueprints.get(
        certification
    )

    if not blueprint_file:
        return {}

    with open(
        blueprint_file,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==========================================
# EXAMEN OFICIAL
# ==========================================

def generate_official_exam(
    db: Session,
    certification: str,
    language: str
):
    """
    Genera examen balanceado según syllabus.
    """

    blueprint = load_blueprint(
        certification
    )

    if not blueprint:

        raise ValueError(
            f"No existe blueprint para {certification}"
        )
    
    questions_per_chapter = (
        blueprint[
            "questions_per_chapter"
            ]
        )

    points_per_chapter = (
        blueprint[
            "points_per_chapter"
        ]
    )

    if set(
        questions_per_chapter.keys()
    ) != set(
        points_per_chapter.keys()
    ):

        raise ValueError(
            f"Blueprint inválido para {certification}"
        )

    expected_questions = sum(
        questions_per_chapter.values()
    )

    selected_questions = []

    used_question_ids = set()

    # ======================================
    # DISTRIBUCIÓN POR CHAPTER
    # ======================================

    for chapter, quantity in (
        questions_per_chapter.items()
    ):

        chapter_questions = db.query(
            Question
        ).filter(
            Question.certification ==
            certification,

            Question.chapter == chapter
        ).all()

        # ==================================
        # ELIMINAR REPETIDAS
        # ==================================

        chapter_questions = [

            question

            for question in chapter_questions

            if question.id not in
            used_question_ids
        ]

        # ==================================
        # AJUSTAR DISPONIBILIDAD
        # ==================================

        available = len(chapter_questions)

        if quantity > available:
            quantity = available

        if quantity == 0:
            continue

        # ==================================
        # RANDOM SAMPLE
        # ==================================

        sampled_questions = random.sample(
            chapter_questions,
            quantity
        )

        for question in sampled_questions:

            used_question_ids.add(
                question.id
            )

        selected_questions.extend(
            sampled_questions
        )

    # ======================================
    # MEZCLAR PREGUNTAS
    # ======================================

    random.shuffle(selected_questions)

    serialized_questions = [

        serialize_question(
            question,
            language
        )

        for question in selected_questions
    ]

    return {
        "total_questions":
            len(serialized_questions),

        "requested_questions": 
            expected_questions,

        "adjusted": False,

        "questions":
            serialized_questions,

        "certification":
            blueprint["certification"],

        "blueprint":
            questions_per_chapter,
    }