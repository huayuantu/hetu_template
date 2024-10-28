from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class Event(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    model_config = ConfigDict(frozen=True)


class Allocated(Event):
    orderid: str
    sku: str
    qty: int
    batchref: str


class Deallocated(Event):
    orderid: str
    sku: str
    qty: int


class OutOfStock(Event):
    sku: str
