from pydantic import BaseModel
from operations.schemas import NewOrder


class Answer(BaseModel):
    status: str | None
    data: list[NewOrder] | None
    details: str | None
