from datetime import datetime

from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.loan_model import Loan
from app.models.user_model import User
from app.models.device_model import Device


def get_all_loans(
    db: Session
):
    return db.query(Loan).all()


def get_loan_by_id(
    db: Session,
    loan_id: int
):
    loan = (
        db.query(Loan)
        .filter(Loan.id == loan_id)
        .first()
    )

    if not loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    return loan


def create_loan(
    db: Session,
    loan_data
):
    user = (
        db.query(User)
        .filter(User.id == loan_data.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    device = (
        db.query(Device)
        .filter(Device.id == loan_data.device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    if not device.is_available:
        raise HTTPException(
            status_code=409,
            detail="Device not available"
        )

    loan = Loan(
        user_id=loan_data.user_id,
        device_id=loan_data.device_id,
        status="active"
    )

    device.is_available = False

    db.add(loan)

    db.commit()

    db.refresh(loan)

    return loan


def return_loan(
    db: Session,
    loan_id: int
):
    loan = get_loan_by_id(
        db,
        loan_id
    )

    if loan.status == "returned":
        raise HTTPException(
            status_code=409,
            detail="Loan already returned"
        )

    loan.status = "returned"

    loan.return_date = datetime.utcnow()

    loan.device.is_available = True

    db.commit()

    db.refresh(loan)


    return loan

def get_loans_details(db: Session):

    loans = (
        db.query(Loan)
        .join(User)
        .join(Device)
        .all()
    )

    result = []

    for loan in loans:

        result.append({
            "loan_id": loan.id,
            "status": loan.status,
            "loan_date": loan.loan_date,
            "return_date": loan.return_date,

            "user": {
                "id": loan.user.id,
                "name": loan.user.name,
                "email": loan.user.email
            },

            "device": {
                "id": loan.device.id,
                "name": loan.device.name,
                "serial_number": loan.device.serial_number,
                "device_type": loan.device.device_type
            }
        })

    return result