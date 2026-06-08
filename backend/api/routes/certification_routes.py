from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db

from services.discovery_service import (
    get_available_certifications,
    get_certification_metadata
)

router = APIRouter(
    prefix="/certifications",
    tags=["Certifications"]
)


@router.get("")
def get_certifications():

    return get_available_certifications()

@router.get(
    "/{certification}/metadata"
)
def get_metadata(
    certification: str,
    db: Session = Depends(get_db)
):

    return get_certification_metadata(
        db,
        certification
    )