import json


def load_certification_config(
    certification
):
    """
    Configuración oficial ISTQB.
    """

    configs = {

        "Foundation Tester":
        "certifications/foundation.json",

        "Automation Tester":
        "certifications/automation.json"
    }

    file_path = configs.get(
        certification
    )

    if not file_path:

        raise ValueError(
            f"Configuración no encontrada para {certification}"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)