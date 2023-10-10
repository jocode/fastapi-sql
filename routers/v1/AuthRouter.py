from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from schemes.pydantic.UserScheme import UserScheme
from utils.jwt_manager import create_token

AuthRouter = APIRouter(
    prefix="/v1/auth", tags=["auth"]
)


@AuthRouter.post("/login",
                 summary="Autenticación de usuarios",
                 description="Autenticación de usuarios para obtener un token de acceso")
def login(user: UserScheme):
    if user.email == "admin@admin.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Credenciales son invalidas"})
