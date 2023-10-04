from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from middlewares.error_handler import ErrorHandler
from models.BaseModel import init_db
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Movies API"
app.version = "0.0.1"
app.description = "API para el manejo de películas"

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

# Initialize Data Model attributes
init_db()


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
