from pydantic import BaseModel

from typing import List


# ==========================================
# SCORE HISTORY
# ==========================================

class ScoreHistoryItem(BaseModel):

    id: int

    certification: str

    score: float

    passed: bool

    created_at: str


# ==========================================
# INCORRECT QUESTION
# ==========================================

class IncorrectQuestionItem(BaseModel):

    question_id: int

    incorrect_count: int


# ==========================================
# GLOBAL STATS
# ==========================================

class GlobalStatisticsResponse(
    BaseModel
):

    total_exams: int

    average_score: float

    passed_exams: int

    failed_exams: int

    pass_rate: float

    score_history: List[
        ScoreHistoryItem
    ]

    incorrect_questions: List[
        IncorrectQuestionItem
    ]