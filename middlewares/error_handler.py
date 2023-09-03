import typing
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request : Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={
                    "message": e.detail,
                    "error": e.__class__.__name__
                }
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "message": f"{e}",
                    "error": e.__class__.__name__
                }
            )