from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.statistics_schema import (
    GlobalStatisticsResponse
)

from services.statistics_service import (
    get_global_statistics
)

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


# ==========================================
# GLOBAL STATS
# ==========================================

@router.get(
    "/global",
    response_model=
        GlobalStatisticsResponse
)
def global_statistics(
    db: Session = Depends(get_db)
):
    """
    Retorna estadísticas globales.
    """

    return get_global_statistics(
        db=db
    )