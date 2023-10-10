from typing import Optional

from pydantic import BaseModel, Field


class MovieSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=15, max_length=100)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    model_config = {
        "json_scheme_extra": {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
    }
