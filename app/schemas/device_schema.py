from pydantic import BaseModel
from pydantic import Field

from datetime import datetime


class DeviceCreate(BaseModel):

    name: str = Field(..., min_length=3)

    serial_number: str

    device_type: str

    brand: str | None = None


class DeviceUpdate(BaseModel):

    name: str = Field(..., min_length=3)

    serial_number: str

    device_type: str

    brand: str | None = None

    is_available: bool


class DevicePatch(BaseModel):

    name: str | None = None

    serial_number: str | None = None

    device_type: str | None = None

    brand: str | None = None

    is_available: bool | None = None


class DeviceResponse(BaseModel):

    id: int

    name: str

    serial_number: str

    device_type: str

    brand: str | None

    is_available: bool

    created_at: datetime

    model_config = {
        "from_attributes": True
    }