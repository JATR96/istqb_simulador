import json
import os


CERTIFICATIONS_PATH = (
    "certifications"
)


def load_certification_config(
    certification
):
    """
    Carga configuración ISTQB.
    """

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

            if (
                config["certification"]
                ==
                certification
            ):
                return config

    raise ValueError(
        f"Certificación no encontrada: {certification}"
    )