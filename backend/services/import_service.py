import json

from sqlalchemy.orm import Session

from models.question_model import Question

"""
Servicio profesional de importación de preguntas.
"""


# ==========================================
# VALIDAR TRADUCCIONES
# ==========================================

def validate_translations(translations):
    """
    Valida estructura multiidioma.
    """

    required_languages = ["es", "en"]

    for language in required_languages:

        if language not in translations:
            raise ValueError(
                f"Idioma faltante: {language}"
            )

        translation = translations[language]

        required_fields = [
            "pregunta",
            "opciones",
            "respuesta_correcta_id",
            "explicacion"
        ]

        for field in required_fields:

            if field not in translation:
                raise ValueError(
                    f"Campo faltante '{field}' en idioma '{language}'"
                )

        options = translation["opciones"]

        if len(options) < 2:
            raise ValueError(
                "La pregunta debe tener al menos 2 opciones"
            )

        option_ids = [
            option["id"]
            for option in options
        ]

        correct_id = translation[
            "respuesta_correcta_id"
        ]

        if correct_id not in option_ids:
            raise ValueError(
                "respuesta_correcta_id inválido"
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

    for question_data in questions_data:

        # ======================================
        # VALIDAR TRANSLATIONS
        # ======================================

        validate_translations(
            question_data["translations"]
        )

        # ======================================
        # EVITAR DUPLICADOS
        # ======================================

        existing_question = db.query(
            Question
        ).filter(
            Question.learning_objective ==
            question_data["learning_objective"]
        ).first()

        if existing_question:
            skipped += 1
            continue

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

            image_url=question_data.get(
                "image_url"
            ),

            image_description=question_data.get(
                "image_description"
            ),

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