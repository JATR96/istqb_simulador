from pydantic import BaseModel
from typing import Optional
from typing import Dict
from typing import List
from typing import Any

"""
Schemas Pydantic para preguntas ISTQB.
"""


# ==========================================
# OPCIÓN RESPUESTA
# ==========================================

class OptionSchema(BaseModel):
    id: int
    texto: str

# ==========================================
# TRADUCCIÓN
# ==========================================

class TranslationSchema(BaseModel):
    
    pregunta: str

    opciones: List[
        OptionSchema
    ]

    explicacion: str

# ==========================================
# QUESTION BASE
# ==========================================

class QuestionBase(BaseModel):

    certification: str

    chapter: str

    section: str

    learning_objective: str

    k_level: str

    points: int

    tipo_pregunta: str

    respuestas_correctas: List[int]

    image_url: Optional[str] = None

    image_description: Optional[str] = None

    translations: Dict[str, Any]

# ==========================================
# CREATE QUESTION
# ==========================================

class QuestionCreate(QuestionBase):
    pass

# ==========================================
# RESPONSE QUESTION
# ==========================================

class QuestionResponse(QuestionBase):

    id: int

    class Config:
        from_attributes = True