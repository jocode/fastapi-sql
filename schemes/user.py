from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str

    model_config = {
        "json_scheme_extra": {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin"
            }
        }
    }
