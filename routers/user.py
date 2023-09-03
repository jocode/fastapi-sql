from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from jwt_manager import create_token

user_router = APIRouter()


class User(BaseModel):
    email: str
    password: str


@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"message": "Credenciales son invalidas"})
