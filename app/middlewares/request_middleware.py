import time
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware


class RequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):
        start_time = time.perf_counter()
        request_id = request.headers.get(
            "X-Request-ID",
            str(uuid4())
        )

        response = await call_next(request)
        process_time = time.perf_counter() - start_time

        response.headers["X-App-Name"] = "device_systems"
        response.headers["X-Process-Time"] = f"{process_time:.4f}"
        response.headers["X-Request-ID"] = request_id

        print(
            f"{request.method} {request.url.path} {response.status_code}"
        )

        return response
