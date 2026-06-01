from fastapi import FastAPI

app = FastAPI(
    title="ISTQB Simulator API",
    version="1.0.0"
)


@app.get("/")
def home():
    """
    Endpoint principal para verificar
    que la API funciona correctamente.
    """
    return {
        "message": "ISTQB Simulator API funcionando correctamente"
    }