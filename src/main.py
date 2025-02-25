from fastapi import FastAPI, status
from .models import Base
from .database import engine
from .routers import admin, auth, todos, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/")
def home():
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {"message": "Healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
