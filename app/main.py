from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware 
from .routers import produce, auth, admins



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(produce.router)
app.include_router(auth.router)
app.include_router(admins.router)


@app.get("/")
def root():
    return {"message": "This is HomeGrown"}