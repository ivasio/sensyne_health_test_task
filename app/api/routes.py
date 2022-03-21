from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter

from .models import ReadingCreateRequest, ReadingResponse, ReadingUpdateRequest


router = APIRouter()


@router.get('/reading', response_model=List[ReadingResponse])
def get_v1_reading() -> List[ReadingResponse]:
    """
    Get all readings
    """
    pass


@router.post('/reading', response_model=None)
def post_v1_reading(body: ReadingCreateRequest) -> None:
    """
    Create a new reading
    """
    pass


@router.get('/reading/{reading_uuid}', response_model=ReadingResponse)
def get_v1_reading_reading_uuid(reading_uuid: UUID) -> ReadingResponse:
    """
    Get a reading by UUID
    """
    pass


@router.put('/reading/{reading_uuid}', response_model=None)
def put_v1_reading_reading_uuid(
    reading_uuid: UUID, body: ReadingUpdateRequest = ...
) -> None:
    """
    Update a reading by UUID
    """
    pass


@router.delete('/reading/{reading_uuid}', response_model=None)
def delete_v1_reading_reading_uuid(reading_uuid: UUID) -> None:
    """
    Delete a reading by UUID
    """
    pass
