from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter

from .models import ReadingCreateRequest, ReadingResponse, ReadingUpdateRequest
from .repositories import ReadingsRepo


router = APIRouter()


@router.get('/reading', response_model=List[ReadingResponse])
def get_v1_reading() -> List[ReadingResponse]:
    """
    Get all readings
    """
    repo = ReadingsRepo()
    result = repo.get_all()
    return result


@router.post('/reading', response_model=None)
def post_v1_reading(body: ReadingCreateRequest) -> None:
    """
    Create a new reading
    """
    repo = ReadingsRepo()
    repo.add(reading=body)


@router.get('/reading/{reading_uuid}', response_model=ReadingResponse)
def get_v1_reading_reading_uuid(reading_uuid: UUID) -> ReadingResponse:
    """
    Get a reading by UUID
    """
    repo = ReadingsRepo()
    result = repo.get(uuid=reading_uuid)
    return result


@router.put('/reading/{reading_uuid}', response_model=None)
def put_v1_reading_reading_uuid(
    reading_uuid: UUID, body: ReadingUpdateRequest = ...
) -> None:
    """
    Update a reading by UUID
    """
    repo = ReadingsRepo()
    repo.update(uuid=reading_uuid, reading=body)


@router.delete('/reading/{reading_uuid}', response_model=None)
def delete_v1_reading_reading_uuid(reading_uuid: UUID) -> None:
    """
    Delete a reading by UUID
    """
    repo = ReadingsRepo()
    repo.delete(uuid=reading_uuid)
