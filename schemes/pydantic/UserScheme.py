from pydantic import BaseModel


class UserScheme(BaseModel):
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
