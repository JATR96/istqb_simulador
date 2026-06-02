from pydantic import BaseModel

from typing import List

from typing import Optional


# ==========================================
# RESPUESTA USUARIO
# ==========================================

class UserAnswerRequest(BaseModel):

    question_id: int

    selected_option_id: int


# ==========================================
# REQUEST RESULTADO
# ==========================================

class SubmitExamRequest(BaseModel):

    certification: str

    language: str

    exam_mode: str

    duration_seconds: Optional[int]

    answers: List[UserAnswerRequest]


# ==========================================
# REVIEW QUESTION
# ==========================================

class ReviewQuestionResponse(BaseModel):

    question_id: int

    question: str

    selected_option_id: int

    correct_option_id: int

    is_correct: bool

    explanation: str


# ==========================================
# RESPONSE RESULTADO
# ==========================================

class SubmitExamResponse(BaseModel):

    score: float

    passed: bool

    total_questions: int

    correct_answers: int

    incorrect_answers: int

    review: List[
        ReviewQuestionResponse
    ]