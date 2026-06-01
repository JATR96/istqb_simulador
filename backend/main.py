from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.health_routes import router as health_router

app = FastAPI(
    title="ISTQB Simulator API",
    version="1.0.0",
    description="API profesional para simulador ISTQB"
)

# ==========================================
# CONFIGURACIÓN CORS
# ==========================================

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# REGISTRO DE ROUTERS
# ==========================================

app.include_router(health_router)


# ==========================================
# ENDPOINT PRINCIPAL
# ==========================================

@app.get("/")
def root():
    """
    Endpoint raíz.
    """

    return {
        "message": "ISTQB Simulator API funcionando"
    }