from pydantic import BaseModel
from operations.schemas import NewOrder


class Answer(BaseModel):
    status: str | None
    data: list[NewOrder] | None
    data_count: int | None
    details: str | None
