import json

from sqlalchemy.orm import Session

from models.question_model import Question

"""
Servicio profesional de importación de preguntas.
"""

# ==========================================
# CONSTANTES
# ==========================================

VALID_K_LEVELS = [
    "K1",
    "K2",
    "K3",
    "K4"
]

# ==========================================
# NORMALIZE TEXT
# ==========================================

def normalize_text(
    question_text: str
):
    """
    Normaliza texto para
    comparación de duplicados.
    """

    return " ".join(
        question_text.lower().split()
    )

# ==========================================
# VALIDAR TRADUCCIONES
# ==========================================

def validate_translations(translations):
    """
    Valida estructura multiidioma.
    """

    required_languages = [
        "es",
        "en"
    ]

    for language in required_languages:

        if language not in translations:

            raise ValueError(
                f"Idioma faltante: {language}"
            )

        translation = translations[
            language
        ]

        required_fields = [
            "pregunta",
            "opciones",
            "explicacion"
        ]

        images = translation.get(
            "imagenes",
            []
        )

        if not isinstance(
            images,
            list
        ):
            raise ValueError(
                f"imagenes debe ser una lista en idioma {language}"
            )

        for image in images:

            if "url" not in image:

                raise ValueError(
                    f"La imagen del idioma {language} debe contener url"
                )

        for field in required_fields:

            if field not in translation:

                raise ValueError(
                    f"Campo faltante '{field}' en idioma '{language}'"
                )

        options = translation[
            "opciones"
        ]

        if len(options) < 2:

            raise ValueError(
                "La pregunta debe tener al menos 2 opciones"
            )

        option_ids = [
            option["id"]
            for option in options
        ]

        if len(option_ids) != len(set(option_ids)):

            raise ValueError(
                "Existen IDs duplicados en las opciones"
            )

# ==========================================
# IMPORTAR JSON
# ==========================================

def import_questions(
    db: Session,
    json_path: str
):
    """
    Importa preguntas desde archivo JSON.
    """

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as file:

        questions_data = json.load(file)

    imported = 0

    skipped = 0

    # ======================================
    # CACHE DE PREGUNTAS EXISTENTES
    # ======================================

    existing_questions = db.query(
        Question
    ).all()

    existing_normalized_questions = set()

    for question in existing_questions:

        try:

            spanish_question = (
                question.translations["es"]["pregunta"]
            )

            existing_normalized_questions.add(
                normalize_text(
                    spanish_question
                )
            )

        except Exception:

            pass

    # ======================================
    # IMPORTACIÓN
    # ======================================

    for question_data in questions_data:

        # ======================================
        # VALIDAR CAMPOS OBLIGATORIOS
        # ======================================

        required_question_fields = [

            "certification",

            "chapter",

            "section",

            "learning_objective",

            "k_level",

            "points",

            "tipo_pregunta",

            "cantidad_respuestas",

            "respuestas_correctas",

            "translations"
        ]

        for field in required_question_fields:

            if field not in question_data:

                raise ValueError(
                    f"Campo faltante: {field}"
                )

        # ======================================
        # VALIDAR TRANSLATIONS
        # ======================================

        validate_translations(
            question_data["translations"]
        )

        # ======================================
        # VALIDAR K-LEVEL
        # ======================================

        if (
            question_data["k_level"]
            not in VALID_K_LEVELS
        ):

            raise ValueError(
                f"K-Level inválido: {question_data['k_level']}"
            )

        # ======================================
        # VALIDAR PUNTOS
        # ======================================

        if question_data["points"] <= 0:

            raise ValueError(
                "points debe ser mayor a cero"
            )

        # ======================================
        # VALIDAR RESPUESTAS CORRECTAS
        # ======================================

        correct_answers = question_data[
            "respuestas_correctas"
        ]

        required_answers = question_data[
            "cantidad_respuestas"
        ]

        if required_answers <= 0:

            raise ValueError(
                "cantidad_respuestas debe ser mayor a cero"
            )

        if len(correct_answers) != required_answers:

            raise ValueError(
                "cantidad_respuestas debe coincidir con respuestas_correctas"
            )

        spanish_options = (
            question_data[
                "translations"
            ]["es"]["opciones"]
        )

        option_ids = [

            option["id"]

            for option
            in spanish_options

        ]

        for answer_id in correct_answers:

            if answer_id not in option_ids:

                raise ValueError(
                    f"Respuesta correcta inválida: {answer_id}"
                )

        # ======================================
        # EVITAR DUPLICADOS REALES
        # ======================================

        normalized_question = normalize_text(

            question_data[
                "translations"
            ]["es"]["pregunta"]

        )

        if normalized_question in (
            existing_normalized_questions
        ):

            skipped += 1

            continue

        existing_normalized_questions.add(
            normalized_question
        )

        # ======================================
        # CREAR QUESTION
        # ======================================

        question = Question(

            certification=question_data[
                "certification"
            ],

            chapter=question_data[
                "chapter"
            ],

            section=question_data[
                "section"
            ],

            learning_objective=question_data[
                "learning_objective"
            ],

            k_level=question_data[
                "k_level"
            ],

            points=question_data[
                "points"
            ],

            tipo_pregunta=question_data[
                "tipo_pregunta"
            ],

            cantidad_respuestas=question_data[
                "cantidad_respuestas"
            ],

            respuestas_correctas=question_data[
                "respuestas_correctas"
            ],

            translations=question_data[
                "translations"
            ]
        )

        db.add(question)

        imported += 1

    db.commit()

    return {

        "imported": imported,

        "skipped": skipped

    }