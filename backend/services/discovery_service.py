import json
import os


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