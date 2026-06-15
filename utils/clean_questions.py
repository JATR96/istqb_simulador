import re


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def process_text(text):
    # ---------------------------------------------------------
    # Eliminar separadores ##################################################
    # ---------------------------------------------------------
    text = re.sub(
        r'^\s*#{10,}\s*$',
        '',
        text,
        flags=re.MULTILINE
    )

    # ---------------------------------------------------------
    # Eliminar líneas vacías entre metadatos
    # ---------------------------------------------------------
    metadata_fields = [
        "CERTIFICATION:",
        "LEARNING_OBJECTIVE:",
        "K_LEVEL:",
        "POINTS:",
        "CANTIDAD_RESPUESTAS:",
        "RESPUESTAS_CORRECTAS:"
    ]

    for field in metadata_fields:
        text = re.sub(
            rf'({re.escape(field)}[^\n]*)\n\s*\n',
            r'\1\n',
            text
        )

    # ---------------------------------------------------------
    # Compactar bloques de opciones
    # ---------------------------------------------------------
    option_pattern = (
        r'([a-z]\)\s.*?)(?:\n\s*\n)(?=[a-z]\)\s)'
    )

    previous = None

    while previous != text:
        previous = text
        text = re.sub(
            option_pattern,
            r'\1\n',
            text,
            flags=re.DOTALL
        )

    # ---------------------------------------------------------
    # Compactar líneas vacías repetidas
    # ---------------------------------------------------------
    text = re.sub(r'\n{3,}', '\n\n', text)

    # ---------------------------------------------------------
    # Eliminar espacios al inicio/final
    # ---------------------------------------------------------
    text = text.strip()

    return text


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    processed = process_text(content)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(processed)

    print(f"Archivo procesado correctamente: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()