from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func

from database import Base

"""
Tabla para almacenar respuestas del usuario.

Esto permitirá:
- estadísticas
- repaso de errores
- historial
- analytics
"""


class UserAnswer(Base):

    __tablename__ = "user_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # ==========================================
    # RELACIÓN EXAMEN
    # ==========================================

    exam_attempt_id = Column(
        Integer,
        ForeignKey("exam_attempts.id"),
        nullable=False
    )

    # ==========================================
    # PREGUNTA
    # ==========================================

    question_id = Column(
        Integer,
        nullable=False
    )

    # ==========================================
    # RESPUESTA USUARIO
    # ==========================================

    selected_option_id = Column(
        Integer,
        nullable=False
    )

    # ==========================================
    # RESULTADO
    # ==========================================

    is_correct = Column(
        Boolean,
        nullable=False
    )

    # ==========================================
    # FECHA
    # ==========================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )