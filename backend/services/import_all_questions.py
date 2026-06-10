import os

from services.import_service import (
    import_questions
)


def import_all_questions(
    db,
    data_directory
):
    """
    Importa todos los JSON
    encontrados dentro de data/.
    """

    total_imported = 0

    total_skipped = 0

    for root, _, files in os.walk(
        data_directory
    ):

        for file in files:

            if not file.endswith(
                ".json"
            ):
                continue

            json_path = os.path.join(
                root,
                file
            )

            print(
                f"Importando: {json_path}"
            )

            result = import_questions(
                db,
                json_path
            )

            total_imported += (
                result["imported"]
            )

            total_skipped += (
                result["skipped"]
            )

    return {

        "imported":
            total_imported,

        "skipped":
            total_skipped
    }