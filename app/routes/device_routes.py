from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import status

from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.dependencies.auth_dependency import (
    require_admin,
    require_roles
)

from app.schemas.device_schema import (
    DeviceCreate,
    DeviceUpdate,
    DevicePatch,
    DeviceResponse
)

from app.services.device_service import (
    get_all_devices,
    get_device_by_id,
    create_device,
    update_device,
    patch_device,
    delete_device
)

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.get(
    "",
    response_model=list[DeviceResponse]
)
def get_devices(
    device_type: str | None = Query(None),
    brand: str | None = Query(None),
    is_available: bool | None = Query(None),
    search: str | None = Query(None),
    db: Session = Depends(get_db)
):
    return get_all_devices(
        db,
        device_type,
        brand,
        is_available,
        search
    )


@router.get(
    "/{device_id}",
    response_model=DeviceResponse
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    return get_device_by_id(
        db,
        device_id
    )


@router.post(
    "",
    response_model=DeviceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_device(
    device: DeviceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "support"))
):
    return create_device(
        db,
        device
    )


@router.put(
    "/{device_id}",
    response_model=DeviceResponse
)
def replace_device(
    device_id: int,
    device: DeviceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "support"))
):
    return update_device(
        db,
        device_id,
        device
    )


@router.patch(
    "/{device_id}",
    response_model=DeviceResponse
)
def modify_device(
    device_id: int,
    device: DevicePatch,
    db: Session = Depends(get_db)
):
    return patch_device(
        db,
        device_id,
        device.model_dump(exclude_unset=True)
    )


@router.delete(
    "/{device_id}"
)
def remove_device(
    device_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return delete_device(
        db,
        device_id
    )
