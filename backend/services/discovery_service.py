import json
import os
from models.question_model import Question

CERTIFICATIONS_PATH = (
    "certifications"
)


def get_available_certifications():
    """
    Obtiene certificaciones disponibles.
    """

    certifications = []

    for file_name in os.listdir(
        CERTIFICATIONS_PATH
    ):

        if not file_name.endswith(
            ".json"
        ):
            continue

        file_path = os.path.join(
            CERTIFICATIONS_PATH,
            file_name
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            config = json.load(file)

            certifications.append(
                config
            )

    return certifications

def get_certification_metadata(
    db,
    certification
):
    """
    Obtiene capítulos y learning objectives
    disponibles para una certificación.
    """

    chapters = db.query(
        Question.chapter
    ).filter(
        Question.certification ==
        certification
    ).distinct().all()

    learning_objectives = db.query(
        Question.learning_objective
    ).filter(
        Question.certification ==
        certification
    ).distinct().all()

    return {

        "chapters": sorted([
            chapter[0]
            for chapter in chapters
        ]),

        "learning_objectives": sorted([
            objective[0]
            for objective in learning_objectives
        ])
    }