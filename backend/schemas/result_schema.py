from pydantic import BaseModel

from typing import List

from typing import Optional


# ==========================================
# RESPUESTA USUARIO
# ==========================================

class UserAnswerRequest(BaseModel):

    question_id: int

    selected_option_ids: List[int]


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

    options: list

    selected_option_ids: List[int]

    correct_option_ids: List[int]

    is_correct: bool

    type: str

    k_level: str

    points: int

    explanation: str

# ==========================================
# RESPONSE RESULTADO
# ==========================================

class SubmitExamResponse(BaseModel):

    score: float

    earned_points: int

    total_points: int

    passing_points: int

    passed: bool

    total_questions: int

    correct_answers: int

    incorrect_answers: int

    review: List[
        ReviewQuestionResponse
    ]