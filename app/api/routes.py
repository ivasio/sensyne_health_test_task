from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from .models import ReadingCreateRequest, ReadingResponse, ReadingUpdateRequest
from .repositories import ReadingsRepo


router = APIRouter()


@router.get('/reading', response_model=List[ReadingResponse])
async def get_v1_reading() -> List[ReadingResponse]:
    """
    Get all readings
    """
    repo = ReadingsRepo()
    result = await repo.get_all()
    return result


@router.post('/reading', response_model=None)
async def post_v1_reading(body: ReadingCreateRequest):
    """
    Create a new reading
    """
    repo = ReadingsRepo()
    result = await repo.add(reading_request=body)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))


@router.get('/reading/{reading_uuid}', response_model=ReadingResponse)
async def get_v1_reading_reading_uuid(reading_uuid: UUID) -> ReadingResponse:
    """
    Get a reading by UUID
    """
    repo = ReadingsRepo()
    result = await repo.get(uuid=reading_uuid)
    return result


@router.put('/reading/{reading_uuid}', response_model=None)
async def put_v1_reading_reading_uuid(
    reading_uuid: UUID, body: ReadingUpdateRequest = ...
):
    """
    Update a reading by UUID
    """
    repo = ReadingsRepo()
    await repo.update(uuid=reading_uuid, reading=body)
    return Response(status_code=204)


@router.delete('/reading/{reading_uuid}', response_model=None)
async def delete_v1_reading_reading_uuid(reading_uuid: UUID):
    """
    Delete a reading by UUID
    """
    repo = ReadingsRepo()
    await repo.delete(uuid=reading_uuid)
    return Response(status_code=204)
