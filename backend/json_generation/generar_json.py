from docx import Document
import json
import re


def clean_text(text):
    return text.strip().replace("\r", "")


def parse_question_block(block):
    lines = [line.strip() for line in block.split("\n")]

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

    current_lang = None
    current_mode = None

    question_text = []
    explanation_text = []
    options = []

    i = 0

    while i < len(lines):
        line = lines[i]

        if not line:
            i += 1
            continue

        # =========================
        # CABECERA
        # =========================

        if line.startswith("CERTIFICATION:"):
            question["certification"] = line.split(":", 1)[1].strip()

        elif line.startswith("CHAPTER:"):
            question["chapter"] = line.split(":", 1)[1].strip()

        elif line.startswith("SECTION:"):
            question["section"] = line.split(":", 1)[1].strip()

        elif line.startswith("LEARNING_OBJECTIVE:"):
            question["learning_objective"] = line.split(":", 1)[1].strip()

        elif line.startswith("K_LEVEL:"):
            question["k_level"] = line.split(":", 1)[1].strip()

        elif line.startswith("POINTS:"):
            question["points"] = int(line.split(":", 1)[1].strip())

        elif line.startswith("RESPUESTAS_CORRECTAS:"):
            raw = line.split(":", 1)[1].strip()

            question["respuestas_correctas"] = [
                int(x.strip())
                for x in raw.split(",")
                if x.strip()
            ]

        elif line.startswith("IMAGE_URL:"):
            value = line.split(":", 1)[1].strip()
            question["image_url"] = value if value else None

        elif line.startswith("IMAGE_DESCRIPTION:"):
            value = line.split(":", 1)[1].strip()
            question["image_description"] = value if value else None

        # =========================
        # IDIOMAS
        # =========================

        elif re.match(r"\[[a-z]{2}\]", line.lower()):
            current_lang = line.replace("[", "").replace("]", "").lower()

            question["translations"][current_lang] = {
                "pregunta": "",
                "opciones": [],
                "explicacion": ""
            }

        elif line.startswith("[/"):
            if current_lang:
                question["translations"][current_lang]["pregunta"] = "\n".join(question_text).strip()

                question["translations"][current_lang]["opciones"] = options

                question["translations"][current_lang]["explicacion"] = "\n".join(explanation_text).strip()

            question_text = []
            explanation_text = []
            options = []

            current_lang = None
            current_mode = None

        # =========================
        # BLOQUES
        # =========================

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

                    idx, text = line.split("|", 1)

                    options.append({
                        "id": int(idx.strip()),
                        "texto": text.strip()
                    })

            elif current_mode == "explanation":
                explanation_text.append(line)

        i += 1

    # =========================
    # TIPO PREGUNTA
    # =========================

    if len(question["respuestas_correctas"]) == 1:
        question["tipo_pregunta"] = "eleccion_simple"
    else:
        question["tipo_pregunta"] = "eleccion_multiple"

    return question


def parse_docx_to_json(docx_file):

    doc = Document(docx_file)

    content = "\n".join(
        p.text
        for p in doc.paragraphs
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


if __name__ == "__main__":

    archivo = "preguntas.docx"

    preguntas = parse_docx_to_json(archivo)

    with open(
        "automation_tester_questions.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            preguntas,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(
        f"Se generaron {len(preguntas)} preguntas correctamente."
    )