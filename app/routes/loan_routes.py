from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db

from app.schemas.loan_schema import (
    LoanCreate,
    LoanResponse
)

from app.services.loan_service import (
    get_all_loans,
    get_loan_by_id,
    create_loan,
    return_loan
)

from app.services.loan_service import (
    get_all_loans,
    get_loan_by_id,
    create_loan,
    return_loan,
    get_loans_details
)

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.get(
    "",
    response_model=list[LoanResponse]
)
def get_loans(
    db: Session = Depends(get_db)
):
    return get_all_loans(db)


@router.get(
    "/{loan_id}",
    response_model=LoanResponse
)
def get_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):
    return get_loan_by_id(
        db,
        loan_id
    )


@router.post(
    "",
    response_model=LoanResponse
)
def create_new_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db)
):
    return create_loan(
        db,
        loan
    )


@router.patch(
    "/{loan_id}/return",
    response_model=LoanResponse
)
def return_device(
    loan_id: int,
    db: Session = Depends(get_db)
):
    return return_loan(
        db,
        loan_id
    )