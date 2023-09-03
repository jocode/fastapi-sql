from fastapi import APIRouter
from starlette.responses import JSONResponse

from jwt_manager import create_token
from schemes.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"message": "Credenciales son invalidas"})
