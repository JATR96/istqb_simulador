from docx import Document
import json
import re


def extract_chapter_section(learning_objective):
    """
    TAE-2.2.1
    -> chapter=2
    -> section=2.2.1
    """

    try:
        section = learning_objective.split("-")[1]
        chapter = section.split(".")[0]

        return chapter, section

    except Exception:
        return "", ""


def parse_question_block(block):

    question = {
        "certification": "",
        "chapter": "",
        "section": "",
        "learning_objective": "",
        "k_level": "",
        "points": 1,
        "image_url": None,
        "image_description": None,
        "tipo_pregunta": "",
        "respuestas_correctas": [],
        "translations": {}
    }

    lines = [line.strip() for line in block.split("\n")]

    current_lang = None
    current_mode = None

    question_text = []
    explanation_text = []
    options = []

    for line in lines:

        if not line:
            continue

        # ==================================================
        # CABECERA
        # ==================================================

        if line.startswith("CERTIFICATION:"):
            question["certification"] = line.split(":", 1)[1].strip()

        elif line.startswith("LEARNING_OBJECTIVE:"):

            lo = line.split(":", 1)[1].strip()

            question["learning_objective"] = lo

            chapter, section = extract_chapter_section(lo)

            question["chapter"] = chapter
            question["section"] = section

        elif line.startswith("K_LEVEL:"):
            question["k_level"] = line.split(":", 1)[1].strip()

        elif line.startswith("POINTS:"):
            question["points"] = int(
                line.split(":", 1)[1].strip()
            )

        elif line.startswith("RESPUESTAS_CORRECTAS:"):

            raw = line.split(":", 1)[1].strip()

            correctas = [
                int(x.strip())
                for x in raw.split(",")
                if x.strip()
            ]

            question["respuestas_correctas"] = correctas

            question["tipo_pregunta"] = (
                "eleccion_simple"
                if len(correctas) == 1
                else "eleccion_multiple"
            )

        elif line.startswith("IMAGE_URL:"):

            value = line.split(":", 1)[1].strip()

            question["image_url"] = (
                value if value else None
            )

        elif line.startswith("IMAGE_DESCRIPTION:"):

            value = line.split(":", 1)[1].strip()

            question["image_description"] = (
                value if value else None
            )

        # ==================================================
        # IDIOMAS
        # ==================================================

        elif re.match(r"\[[a-z]{2}\]", line.lower()):

            current_lang = (
                line.replace("[", "")
                .replace("]", "")
                .lower()
            )

            question["translations"][current_lang] = {
                "pregunta": "",
                "opciones": [],
                "explicacion": ""
            }

        elif line.startswith("[/"):

            question["translations"][current_lang] = {
                "pregunta": "\n".join(question_text).strip(),
                "opciones": options,
                "explicacion": "\n".join(explanation_text).strip()
            }

            current_lang = None
            current_mode = None

            question_text = []
            explanation_text = []
            options = []

        # ==================================================
        # SECCIONES
        # ==================================================

        elif line.upper() in ["PREGUNTA:", "QUESTION:"]:
            current_mode = "question"

        elif line.upper() in ["OPCIONES:", "OPTIONS:"]:
            current_mode = "options"

        elif line.upper() in ["EXPLICACION:", "EXPLANATION:"]:
            current_mode = "explanation"

        else:

            if current_mode == "question":
                question_text.append(line)

            elif current_mode == "options":

                if "|" in line:

                    option_id, option_text = line.split("|", 1)

                    options.append({
                        "id": int(option_id.strip()),
                        "texto": option_text.strip()
                    })

            elif current_mode == "explanation":
                explanation_text.append(line)

    return question


def parse_docx(docx_path):

    doc = Document(docx_path)

    content = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    blocks = re.findall(
        r"=== QUESTION START ===(.*?)=== QUESTION END ===",
        content,
        re.DOTALL
    )

    questions = []

    for block in blocks:
        questions.append(
            parse_question_block(block)
        )

    return questions


def save_json(data, output_file):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


if __name__ == "__main__":

    INPUT_DOCX = "preguntas.docx"
    OUTPUT_JSON = "automation_tester_questions.json"

    preguntas = parse_docx(INPUT_DOCX)

    save_json(
        preguntas,
        OUTPUT_JSON
    )

    print(
        f"Preguntas procesadas: {len(preguntas)}"
    )

    print(
        f"Archivo generado: {OUTPUT_JSON}"
    )