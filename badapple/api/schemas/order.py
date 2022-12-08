from pydantic import BaseModel , Field
from typing import List
from datetime import datetime
from enum import Enum

class StatusEnum(Enum):
    WAITING = "waiting"
    PENDING = "pending"
    SUCCESS = "success"
    CANCELLED = "cancelled"


class ItemSchema(BaseModel):
    product_id: str
    # quantities: int = Field(gt=0, description="The qunatities must be greater than zero")
    quantities: int 

class OrderLineInSchema(BaseModel):
    items: List[ItemSchema]

class OrderLineOutSchema(BaseModel):
    order_id: str
    items: List[ItemSchema]
    total_prices: float
    status: StatusEnum
    timestamp: datetime
