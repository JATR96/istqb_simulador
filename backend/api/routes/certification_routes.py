from fastapi import APIRouter

from services.discovery_service import (
    get_available_certifications
)

router = APIRouter(
    prefix="/certifications",
    tags=["Certifications"]
)


@router.get("")
def get_certifications():

    return get_available_certifications()