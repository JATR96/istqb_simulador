import json
import re
from docx import Document


# =====================================================
# UTILIDADES
# =====================================================

def leer_word(ruta):
    doc = Document(ruta)

    texto = []

    for p in doc.paragraphs:
        texto.append(p.text)

    return "\n".join(texto)


def obtener_chapter(lo):

    try:
        return lo.split("-")[1].split(".")[0]

    except Exception:
        return ""


def obtener_section(lo):
    return lo.split("-")[1]


def detectar_tipo(respuestas):

    if len(respuestas) > 1:
        return "eleccion_multiple"

    return "eleccion_simple"


# =====================================================
# RESPUESTAS CORRECTAS
# =====================================================

def parsear_respuestas(texto):

    mapping = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }

    respuestas = []

    for item in texto.split(","):

        item = item.strip().lower()

        if not item:
            continue

        if item.isdigit():

            respuestas.append(int(item))

        elif item in mapping:

            respuestas.append(mapping[item])

    return respuestas


# =====================================================
# OPCIONES
# =====================================================

def parsear_opciones(texto):

    opciones = []

    patron = r'([a-z])\)\s*(.*?)(?=\n[a-z]\)|$)'

    matches = re.findall(
        patron,
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

    for letra, contenido in matches:

        opciones.append({
            "id": ord(letra.lower()) - ord("a") + 1,
            "texto": " ".join(
                contenido.strip().split()
            )
        })

    return opciones


# =====================================================
# BLOQUE IDIOMA
# =====================================================

def extraer_bloque(texto, idioma):

    patron = rf'\[{idioma}\](.*?)\[/{idioma}\]'

    match = re.search(
        patron,
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

    if not match:
        return None

    return match.group(1).strip()


def parsear_bloque_es(texto):

    pregunta = re.search(
        r'PREGUNTA:\s*(.*?)\s*OPCIONES:',
        texto,
        re.DOTALL
    )

    opciones = re.search(
        r'OPCIONES:\s*(.*?)\s*EXPLICACION:',
        texto,
        re.DOTALL
    )

    explicacion = re.search(
        r'EXPLICACION:\s*(.*)',
        texto,
        re.DOTALL
    )

    return {
        "pregunta": pregunta.group(1).strip(),
        "opciones": parsear_opciones(
            opciones.group(1)
        ),
        "explicacion": explicacion.group(1).strip()
    }


def parsear_bloque_en(texto):

    pregunta = re.search(
        r'QUESTION:\s*(.*?)\s*OPTIONS:',
        texto,
        re.DOTALL
    )

    opciones = re.search(
        r'OPTIONS:\s*(.*?)\s*EXPLANATION:',
        texto,
        re.DOTALL
    )

    explicacion = re.search(
        r'EXPLANATION:\s*(.*)',
        texto,
        re.DOTALL
    )

    return {
        "pregunta": pregunta.group(1).strip(),
        "opciones": parsear_opciones(
            opciones.group(1)
        ),
        "explicacion": explicacion.group(1).strip()
    }


# =====================================================
# CABECERA
# =====================================================

def obtener_campo(nombre, texto):

    for linea in texto.splitlines():

        linea = linea.strip()

        if linea.startswith(f"{nombre}:"):

            valor = linea[len(f"{nombre}:"):].strip()

            return valor

    return ""

# =====================================================
# IDIOMA
# =====================================================

def parsear_bloque_generico(
        texto,
        pregunta_tag,
        opciones_tag,
        explicacion_tag
):

    pregunta = re.search(
        rf'{pregunta_tag}:\s*(.*?)\s*{opciones_tag}:',
        texto,
        re.DOTALL
    )

    opciones = re.search(
        rf'{opciones_tag}:\s*(.*?)\s*{explicacion_tag}:',
        texto,
        re.DOTALL
    )

    explicacion = re.search(
        rf'{explicacion_tag}:\s*(.*)',
        texto,
        re.DOTALL
    )

    return {
        "pregunta":
            pregunta.group(1).strip()
            if pregunta else "",

        "opciones":
            parsear_opciones(
                opciones.group(1)
            ) if opciones else [],

        "explicacion":
            explicacion.group(1).strip()
            if explicacion else ""
    }

# =====================================================
# PARSEAR PREGUNTA
# =====================================================

def parsear_pregunta(texto):

    certification = obtener_campo(
        "CERTIFICATION",
        texto
    )

    learning_objective = obtener_campo(
        "LEARNING_OBJECTIVE",
        texto
    )

    k_level = obtener_campo(
        "K_LEVEL",
        texto
    )

    points = obtener_campo(
        "POINTS",
        texto
    )

    respuestas_correctas = obtener_campo(
        "RESPUESTAS_CORRECTAS",
        texto
    )

    image_url = obtener_campo(
        "IMAGE_URL",
        texto
    )

    image_description = obtener_campo(
        "IMAGE_DESCRIPTION",
        texto
    )

    respuestas = parsear_respuestas(
        respuestas_correctas
    )

    resultado = {
        "certification": certification,

        "chapter":
            obtener_chapter(
                learning_objective
            ),

        "section":
            obtener_section(
                learning_objective
            ),

        "learning_objective":
            learning_objective,

        "k_level":
            k_level,

        "points":
            int(points)
            if points else 1,

        "image_url":
            image_url
            if image_url else None,

        "image_description":
            image_description
            if image_description else None,

        "tipo_pregunta":
            detectar_tipo(
                respuestas
            ),

        "respuestas_correctas":
            respuestas,

        "translations": {}
    }

    # Español

    bloque_es = extraer_bloque(
        texto,
        "es"
    )

    if bloque_es:

        resultado["translations"]["es"] = (
            parsear_bloque_generico(
                bloque_es,
                "PREGUNTA",
                "OPCIONES",
                "EXPLICACION"
            )
        )

    # Inglés

    bloque_en = extraer_bloque(
        texto,
        "en"
    )

    if bloque_en:

        resultado["translations"]["en"] = (
            parsear_bloque_generico(
                bloque_en,
                "QUESTION",
                "OPTIONS",
                "EXPLANATION"
            )
        )

    # Portugués (futuro)

    bloque_pt = extraer_bloque(
        texto,
        "pt"
    )

    if bloque_pt:

        resultado["translations"]["pt"] = (
            parsear_bloque_generico(
                bloque_pt,
                "QUESTION",
                "OPTIONS",
                "EXPLANATION"
            )
        )

    return resultado

# =====================================================
# GENERAR JSON
# =====================================================

def generar_json(ruta_docx):

    contenido = leer_word(
        ruta_docx
    )

    bloques = [
        b.strip()
        for b in contenido.split("---")
        if b.strip()
    ]

    preguntas = []

    for bloque in bloques:

        preguntas.append(
            parsear_pregunta(
                bloque
            )
        )

    return preguntas


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    preguntas = generar_json(
        "preguntas.docx"
    )

    with open(
        "preguntas_generadas.json",
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
        f"Preguntas generadas: {len(preguntas)}"
    )