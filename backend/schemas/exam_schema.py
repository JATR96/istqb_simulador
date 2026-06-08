from pydantic import BaseModel
from typing import List
from typing import Optional

# ==========================================
# REQUEST EXAMEN
# ==========================================

class GenerateExamRequest(BaseModel):
    certification: str
    language: str = "es"
    exam_mode: str
    question_count: Optional[int] = 10
    chapters: Optional[List[str]] = None
    learning_objectives: Optional[
        List[str]
    ] = None

# ==========================================
# RESPUESTA OPCIÓN
# ==========================================

class OptionResponse(BaseModel):
    id: int
    texto: str

# ==========================================
# RESPUESTA QUESTION
# ==========================================

class ExamQuestionResponse(BaseModel):
    id: int
    type: str
    k_level: str
    points: int
    question: str
    options: List[OptionResponse]
    image_url: Optional[str] = None
    image_description: Optional[str] = None
    chapter: str
    section: str
    learning_objective: str

# ==========================================
# RESPUESTA EXAMEN
# ==========================================

class GenerateExamResponse(BaseModel):
    certification: str
    blueprint: dict
    total_questions: int
    requested_questions: int
    adjusted: bool
    questions: List[
        ExamQuestionResponse
    ]