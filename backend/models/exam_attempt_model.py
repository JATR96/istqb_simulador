from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func

from database import Base

"""
Modelo de intentos de examen.

Aquí almacenaremos:
- certificación
- modo examen
- puntaje
- idioma
- duración
- estadísticas
"""


class ExamAttempt(Base):
    """
    Tabla de intentos de examen.
    """

    __tablename__ = "exam_attempts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # ==========================================
    # CERTIFICACIÓN
    # ==========================================

    certification = Column(
        String(100),
        nullable=False
    )

    # ==========================================
    # MODO DE EXAMEN
    # ==========================================

    exam_mode = Column(
        String(100),
        nullable=False
    )

    # ==========================================
    # IDIOMA
    # ==========================================

    language = Column(
        String(10),
        nullable=False,
        default="es"
    )

    # ==========================================
    # RESULTADOS
    # ==========================================

    total_questions = Column(
        Integer,
        nullable=False
    )

    correct_answers = Column(
        Integer,
        nullable=False
    )

    incorrect_answers = Column(
        Integer,
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    passed = Column(
        Boolean,
        default=False
    )

    # ==========================================
    # TIEMPO
    # ==========================================

    duration_seconds = Column(
        Integer,
        nullable=True
    )

    # ==========================================
    # FECHAS
    # ==========================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )