from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from database import Base

# ==========================================
# IMPORTAR MODELOS
# ==========================================

from models import ExamAttempt
from models import UserAnswer

# ==========================================
# ROUTERS
# ==========================================

from api.routes.health_routes import router as health_router

# ==========================================
# CREAR TABLAS
# ==========================================

Base.metadata.create_all(bind=engine)

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

# ==========================================
# ROOT
# ==========================================

@app.get("/")
def root():

    return {
        "message": "ISTQB Simulator API funcionando"
    }