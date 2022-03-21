from typing import List
from uuid import UUID

from .models import ReadingCreateRequest, ReadingResponse, ReadingUpdateRequest


class ReadingsRepo:
    def get_all(self) -> List[ReadingResponse]:
        ...

    def add(self, *, reading: ReadingCreateRequest) -> None:
        ...

    def get(self, uuid: UUID) -> ReadingResponse:
        pass

    def update(self, uuid: UUID, reading: ReadingUpdateRequest) -> None:
        ...

    def delete(self, uuid: UUID):
        ...
