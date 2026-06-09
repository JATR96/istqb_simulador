import json
import re
from docx import Document
from validar_banco_preguntas import validar_banco

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

    try:
        return lo.split("-")[1]

    except Exception:
        return ""


def detectar_tipo(respuestas):

    if len(respuestas) > 1:
        return "eleccion_multiple"

    return "eleccion_simple"


# =====================================================
# VALIDACIONES
# =====================================================

def validar_opciones(opciones):

    ids = sorted(
        [o["id"] for o in opciones]
    )

    if not ids:
        raise Exception(
            "No se encontraron opciones"
        )

    esperado = list(
        range(
            min(ids),
            max(ids) + 1
        )
    )

    if ids != esperado:

        raise Exception(
            f"Opciones inválidas. Esperado {esperado} pero encontró {ids}"
        )

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

            respuestas.append(
                int(item)
            )

        elif item in mapping:

            respuestas.append(
                mapping[item]
            )

    return respuestas


# =====================================================
# OPCIONES
# =====================================================

def parsear_opciones(texto):

    opciones = []

    patron = r'^\s*([a-z])\)\s*(.*?)\s*(?=^\s*[a-z]\)|\Z)'

    matches = re.findall(
        patron,
        texto,
        flags=re.DOTALL | re.MULTILINE | re.IGNORECASE
    )

    for letra, contenido in matches:

        opciones.append({
            "id": ord(letra.lower()) - ord("a") + 1,
            "texto": " ".join(
                contenido.strip().split()
            )
        })

    validar_opciones(opciones)

    return opciones

# =====================================================
# PARSEAR IMÁGENES
# =====================================================

def parsear_imagenes(texto):

    imagenes = []

    if not texto:
        return imagenes

    for linea in texto.splitlines():

        linea = linea.strip()

        if not linea:
            continue

        partes = linea.split("|", 1)

        imagenes.append({

            "url": partes[0].strip(),

            "description":
                partes[1].strip()
                if len(partes) > 1
                else ""
        })

    return imagenes

# =====================================================
# BLOQUES DE PREGUNTAS
# =====================================================

def obtener_bloques(contenido):

    bloques = re.findall(
        r'=== QUESTION START ===(.*?)=== QUESTION END ===',
        contenido,
        flags=re.DOTALL
    )

    if bloques:

        return [
            b.strip()
            for b in bloques
            if b.strip()
        ]

    return [
        b.strip()
        for b in contenido.split("---")
        if b.strip()
    ]


# =====================================================
# CAMPOS CABECERA
# =====================================================

def obtener_campo(nombre, texto):

    for linea in texto.splitlines():

        linea = linea.strip()

        if linea.startswith(f"{nombre}:"):

            return linea.replace(
                f"{nombre}:",
                "",
                1
            ).strip()

    return ""

# =====================================================
# IDIOMAS
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


def parsear_bloque_generico(
        texto,
        pregunta_tag,
        opciones_tag,
        explicacion_tag
):

    pregunta = re.search(
        rf'{pregunta_tag}:\s*(.*?)\s*IMAGES:',
        texto,
        re.DOTALL | re.IGNORECASE
    )

    imagenes = re.search(
        rf'IMAGES:\s*(.*?)\s*{opciones_tag}:',
        texto,
        re.DOTALL | re.IGNORECASE
    )

    opciones = re.search(
        rf'{opciones_tag}:\s*(.*?)\s*{explicacion_tag}:',
        texto,
        re.DOTALL | re.IGNORECASE
    )

    explicacion = re.search(
        rf'{explicacion_tag}:\s*(.*)',
        texto,
        re.DOTALL | re.IGNORECASE
    )

    imagenes_parseadas = (
        parsear_imagenes(
            imagenes.group(1)
        )
        if imagenes
        else []
    )

    return {

        "pregunta":
            pregunta.group(1).strip()
            if pregunta else "",

        "opciones":
            parsear_opciones(
                opciones.group(1)
            ) if opciones else [],

        "imagenes":
            imagenes_parseadas,

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

    respuestas = parsear_respuestas(
        respuestas_correctas
    )

    resultado = {

        "certification":
            certification,

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

        "tipo_pregunta":
            detectar_tipo(
                respuestas
            ),

        "respuestas_correctas":
            respuestas,

        "translations": {}
    }

    # =====================
    # ESPAÑOL
    # =====================

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

    # =====================
    # INGLÉS
    # =====================

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

    # =====================
    # PORTUGUÉS (FUTURO)
    # =====================

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

    contenido = leer_word(ruta_docx)

    bloques = obtener_bloques(
        contenido
    )

    print(
        f"Preguntas encontradas: {len(bloques)}"
    )

    preguntas = []

    for i, bloque in enumerate(bloques, start=1):

        try:

            preguntas.append(
                parsear_pregunta(
                    bloque
                )
            )

        except Exception as e:

            print(
                f"Error en pregunta {i}: {e}"
            )

    return preguntas


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    preguntas = generar_json(
        "preguntas.docx"
    )

    errores = validar_banco(
        preguntas
    )

    if errores > 0:

        print(
            "\n❌ JSON NO generado."
        )

        print(
            "Corrige los errores primero."
        )

        exit()

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
        f"\n✅ JSON generado correctamente con {len(preguntas)} preguntas"
    )