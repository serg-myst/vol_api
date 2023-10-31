from pydantic import BaseModel
from datetime import datetime


class NewOrder(BaseModel):
    orderId: int
    send: bool
    sendAt: datetime
