from fastapi import FastAPI
from .routers import users
from .routers import travels
app = FastAPI()

app.include_router(users.router)
app.include_router(travel_plan.router)

@app.get("/")
def base():
    return {"Travel Plan":"Heru"}