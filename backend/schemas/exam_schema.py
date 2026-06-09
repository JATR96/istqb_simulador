from pydantic import BaseModel
from typing import List
from typing import Optional
from pydantic import Field

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
# RESPUESTA IMAGEN
# ==========================================

class ImageResponse(BaseModel):
    url: str
    description: Optional[str] = None

# ==========================================
# RESPUESTA QUESTION
# ==========================================

class ExamQuestionResponse(BaseModel):
    id: int
    type: str
    correct_answers_count: int
    k_level: str
    points: int
    question: str
    options: List[OptionResponse]
    images: List[ImageResponse] = Field(default_factory=list)
    chapter: str
    section: str
    learning_objective: str

# ==========================================
# RESPUESTA EXAMEN
# ==========================================

class GenerateExamResponse(BaseModel):
    certification: Optional[str] = None
    blueprint: Optional[dict] = None
    total_questions: int
    requested_questions: int
    adjusted: bool
    questions: List[
        ExamQuestionResponse
    ]