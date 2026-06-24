from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import or_

from app.models.device_model import Device


def get_all_devices(
    db: Session,
    device_type=None,
    brand=None,
    is_available=None,
    search=None
):
    query = db.query(Device)

    if device_type:
        query = query.filter(
            Device.device_type == device_type
        )

    if brand:
        query = query.filter(
            Device.brand.ilike(f"%{brand}%")
        )

    if is_available is not None:
        query = query.filter(
            Device.is_available == is_available
        )

    if search:
        query = query.filter(
            or_(
                Device.name.ilike(f"%{search}%"),
                Device.brand.ilike(f"%{search}%")
            )
        )

    return query.all()


def get_device_by_id(
    db: Session,
    device_id: int
):
    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device


def create_device(
    db: Session,
    device_data
):
    existing = (
        db.query(Device)
        .filter(
            Device.serial_number
            == device_data.serial_number
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Serial number already exists"
        )

    device = Device(
        **device_data.model_dump()
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


def update_device(
    db: Session,
    device_id: int,
    device_data
):
    device = get_device_by_id(
        db,
        device_id
    )

    device.name = device_data.name
    device.serial_number = device_data.serial_number
    device.device_type = device_data.device_type
    device.brand = device_data.brand
    device.is_available = device_data.is_available

    db.commit()
    db.refresh(device)

    return device


def patch_device(
    db: Session,
    device_id: int,
    update_data: dict
):
    device = get_device_by_id(
        db,
        device_id
    )

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided"
        )

    for key, value in update_data.items():
        setattr(device, key, value)

    db.commit()
    db.refresh(device)

    return device


def delete_device(
    db: Session,
    device_id: int
):
    device = get_device_by_id(
        db,
        device_id
    )

    db.delete(device)

    db.commit()

    return {
        "message": "Device deleted"
    }