from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.dependencies.auth_dependency import (
    get_current_active_user,
    require_roles,
    limiter
)

from app.schemas.loan_schema import (
    LoanCreate,
    LoanResponse
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
    "/details"
)
def get_loan_details(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "support"))
):
    return get_loans_details(db)


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
@limiter.limit("10/minute")
def create_new_loan(
    request: Request,
    loan: LoanCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
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
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "support"))
):
    return return_loan(
        db,
        loan_id
    )
