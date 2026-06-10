import os

# ==========================================

# CONFIGURACIÓN

# ==========================================

RUTA_PROYECTO = r"C:\Users\USER\Desktop\PROYECTOS\istqb_simulador"

ARCHIVO_SALIDA = "estructura_proyecto.txt"

EXCLUIR = {
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
    ".coverage",
    "coverage",
    "target",
    "out"
}

# ==========================================

# GENERAR ÁRBOL

# ==========================================

def generar_arbol(ruta, nivel=0):
    resultado = ""

    try:
        elementos = sorted(os.listdir(ruta))

        for elemento in elementos:
            if elemento in EXCLUIR:
                continue

            ruta_completa = os.path.join(ruta, elemento)

            resultado += "    " * nivel + elemento

            if os.path.isdir(ruta_completa):
                resultado += "/"

            resultado += "\n"

            if os.path.isdir(ruta_completa):
                resultado += generar_arbol(ruta_completa, nivel + 1)

    except PermissionError:
        resultado += "    " * nivel + "[SIN PERMISOS]\n"

    return resultado

# ==========================================

# MAIN

# ==========================================

if __name__ == "__main__":
    nombre_raiz = os.path.basename(RUTA_PROYECTO)

    contenido = (
        nombre_raiz
        + "/\n"
        + generar_arbol(RUTA_PROYECTO)
    )

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print(f"Archivo generado: {ARCHIVO_SALIDA}")
