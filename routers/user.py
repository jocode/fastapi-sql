from fastapi import APIRouter
from starlette.responses import JSONResponse

from schemes.pydantic.UserScheme import UserScheme
from utils.jwt_manager import create_token

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: UserScheme):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"message": "Credenciales son invalidas"})
