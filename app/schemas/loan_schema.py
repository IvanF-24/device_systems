from pydantic import BaseModel
from datetime import datetime


class LoanCreate(BaseModel):

    user_id: int

    device_id: int


class LoanResponse(BaseModel):

    id: int

    user_id: int

    device_id: int

    status: str

    loan_date: datetime

    return_date: datetime | None

    model_config = {
        "from_attributes": True
    }