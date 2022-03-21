from typing import List
from uuid import UUID, uuid4

from .models import ReadingCreateRequest, ReadingResponse, ReadingUpdateRequest
from .db import readings, database


class ReadingsRepo:
    @staticmethod
    async def get_all() -> List[ReadingResponse]:
        query = readings.select()
        rows = await database.fetch_all(query)
        result = [ReadingResponse.from_orm(row) for row in rows]
        return result

    @staticmethod
    async def add(*, reading_request: ReadingCreateRequest) -> ReadingResponse:
        reading = ReadingResponse.from_orm(reading_request)
        query = readings.insert().values(**reading.dict())
        await database.execute(query)
        return reading

    @staticmethod
    async def get(*, uuid: UUID) -> ReadingResponse:
        query = readings.select().where(reading_uuid=uuid)
        row = await database.fetch_one(query)
        result = ReadingResponse.from_orm(row)
        return result

    @staticmethod
    async def update(uuid: UUID, reading: ReadingUpdateRequest) -> None:
        query = readings.update().where(reading_uuid=uuid).values(**reading.dict(exclude_none=True))
        await database.execute(query)

    @staticmethod
    async def delete(uuid: UUID):
        query = readings.delete().where(reading_uuid=uuid)
        await database.execute(query)
