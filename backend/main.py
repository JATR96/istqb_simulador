from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ==========================================
# IMPORTAR MODELOS
# ==========================================

from models import ExamAttempt
from models import UserAnswer
from models import Question

# ==========================================
# ROUTERS
# ==========================================

from api.routes.health_routes import router as health_router
from api.routes.question_routes import router as question_router
from api.routes.import_routes import router as import_router

# ==========================================
# FASTAPI
# ==========================================

app = FastAPI(
    title="ISTQB Simulator API",
    version="1.0.0",
    description="API profesional para simulador ISTQB"
)

# ==========================================
# CORS
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
# ROUTERS
# ==========================================

app.include_router(health_router)

app.include_router(question_router)

app.include_router(import_router)

# ==========================================
# ROOT
# ==========================================

@app.get("/")
def root():

    return {
        "message": "ISTQB Simulator API funcionando"
    }