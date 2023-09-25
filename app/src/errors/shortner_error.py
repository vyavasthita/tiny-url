from fastapi import Request, status
from fastapi.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class ShortnerException(Exception):
    message: str | None = None


def shortner_validation_exception_handler(request: Request, exc: ShortnerException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": exc.message},
    )
