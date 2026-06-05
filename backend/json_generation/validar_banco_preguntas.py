import re


# =====================================================
# OPCIONES
# =====================================================

def validar_opciones(opciones):

    ids = [o["id"] for o in opciones]

    esperado = list(
        range(1, len(ids) + 1)
    )

    if sorted(ids) != esperado:

        raise Exception(
            f"Opciones inválidas. "
            f"Esperado {esperado}, "
            f"encontrado {ids}"
        )


# =====================================================
# EXPLICACIONES
# =====================================================

def validar_explicaciones(
        opciones,
        explicacion
):

    letras_opciones = {
        chr(96 + o["id"])
        for o in opciones
    }

    letras_explicacion = set(

        re.findall(
            r'^\s*([a-z])\)',
            explicacion,
            flags=re.MULTILINE
                   | re.IGNORECASE
        )

    )

    if letras_opciones != letras_explicacion:

        raise Exception(
            f"""
Opciones:
{sorted(letras_opciones)}

Explicaciones:
{sorted(letras_explicacion)}
"""
        )


# =====================================================
# RESPUESTAS CORRECTAS
# =====================================================

def validar_respuestas_correctas(
        respuestas_correctas,
        opciones
):

    ids_opciones = {
        o["id"]
        for o in opciones
    }

    for respuesta in respuestas_correctas:

        if respuesta not in ids_opciones:

            raise Exception(
                f"Respuesta correcta "
                f"{respuesta} "
                f"no existe"
            )


# =====================================================
# DUPLICADOS
# =====================================================

def validar_opciones_duplicadas(
        opciones
):

    textos = []

    for opcion in opciones:

        texto = opcion["texto"] \
            .strip() \
            .lower()

        if texto in textos:

            raise Exception(
                f"Opción duplicada: "
                f"{texto}"
            )

        textos.append(texto)


# =====================================================
# SIMPLE / MULTIPLE
# =====================================================

def validar_tipo_pregunta(
        tipo,
        respuestas
):

    if (
        tipo == "eleccion_simple"
        and len(respuestas) != 1
    ):

        raise Exception(
            "Pregunta simple "
            "con múltiples "
            "respuestas correctas"
        )

    if (
        tipo == "eleccion_multiple"
        and len(respuestas) < 2
    ):

        raise Exception(
            "Pregunta múltiple "
            "con una sola "
            "respuesta correcta"
        )


# =====================================================
# CAMPOS OBLIGATORIOS
# =====================================================

def validar_campos(
        pregunta
):

    obligatorios = [

        "certification",
        "learning_objective",
        "k_level",
        "points"

    ]

    for campo in obligatorios:

        if not pregunta.get(campo):

            raise Exception(
                f"Campo obligatorio "
                f"faltante: {campo}"
            )


# =====================================================
# K LEVEL
# =====================================================

def validar_k_level(
        k_level
):

    validos = {

        "K1",
        "K2",
        "K3",
        "K4"

    }

    if k_level.upper() \
            not in validos:

        raise Exception(
            f"K-Level inválido: "
            f"{k_level}"
        )


# =====================================================
# PUNTOS
# =====================================================

def validar_points(
        points
):

    if points <= 0:

        raise Exception(
            f"Puntaje inválido: "
            f"{points}"
        )


# =====================================================
# LEARNING OBJECTIVE
# =====================================================

def validar_learning_objective(
        lo
):

    patron = r'^[A-Z]+-\d+\.\d+\.\d+$'

    if not re.match(
            patron,
            lo
    ):

        raise Exception(
            f"Learning Objective "
            f"inválido: {lo}"
        )


# =====================================================
# TRADUCCION
# =====================================================

def validar_traduccion(
        idioma,
        datos,
        respuestas_correctas
):

    opciones = datos["opciones"]

    validar_opciones(
        opciones
    )

    validar_opciones_duplicadas(
        opciones
    )

    validar_explicaciones(
        opciones,
        datos["explicacion"]
    )

    validar_respuestas_correctas(
        respuestas_correctas,
        opciones
    )


# =====================================================
# PREGUNTA COMPLETA
# =====================================================

def validar_pregunta(
        pregunta,
        numero
):

    validar_campos(
        pregunta
    )

    validar_k_level(
        pregunta["k_level"]
    )

    validar_points(
        pregunta["points"]
    )

    validar_learning_objective(
        pregunta[
            "learning_objective"
        ]
    )

    validar_tipo_pregunta(

        pregunta[
            "tipo_pregunta"
        ],

        pregunta[
            "respuestas_correctas"
        ]

    )

    for idioma, datos in \
            pregunta[
                "translations"
            ].items():

        validar_traduccion(

            idioma,

            datos,

            pregunta[
                "respuestas_correctas"
            ]

        )

    print(
        f"✅ Pregunta {numero} OK"
    )


# =====================================================
# BANCO COMPLETO
# =====================================================

def validar_banco(
        preguntas
):

    errores = 0

    for i, pregunta in enumerate(
            preguntas,
            start=1
    ):

        try:

            validar_pregunta(
                pregunta,
                i
            )

        except Exception as e:

            errores += 1

            print(
                f"\n❌ Pregunta {i}"
            )

            print(e)

    print()

    print(
        f"Preguntas: "
        f"{len(preguntas)}"
    )

    print(
        f"Errores: "
        f"{errores}"
    )

    print(
        f"Correctas: "
        f"{len(preguntas)-errores}"
    )

    return errores