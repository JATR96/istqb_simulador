from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import func

from database import Base

"""
Modelo principal de preguntas ISTQB.

Soporta:
- multiidioma
- imágenes
- learning objectives
- K level
- puntos
- tipo de pregunta
- respuestas correctas (para preguntas con múltiples respuestas correctas)
- múltiples certificaciones
"""


class Question(Base):

    __tablename__ = "questions"

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
        nullable=False,
        index=True
    )

    # ==========================================
    # CAPÍTULO
    # ==========================================

    chapter = Column(
        String(50),
        nullable=False,
        index=True
    )

    # ==========================================
    # SECCIÓN
    # ==========================================

    section = Column(
        String(50),
        nullable=False
    )

    # ==========================================
    # LEARNING OBJECTIVE
    # ==========================================

    learning_objective = Column(
        String(100),
        nullable=False,
        index=True
    )

    # ==========================================
    # K LEVEL, PUNTOS, TIPO DE PREGUNTA, RESPUESTAS CORRECTAS
    # ==========================================

    k_level = Column(
        String(10),
        nullable=False
    )

    points = Column(
        Integer,
        default=1
    )

    tipo_pregunta = Column(
        String(50),
        nullable=False
    )

    respuestas_correctas = Column(
        JSON,
        nullable=False
    )

    # ==========================================
    # TRADUCCIONES JSON
    # ==========================================

    translations = Column(
        JSON,
        nullable=False
    )

    # ==========================================
    # FECHAS
    # ==========================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    ) 