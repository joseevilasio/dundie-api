from .routes import main_router
from fastapi import FastAPI


app = FastAPI(
    title="dundie",
    version="0.1.0",
    description="dundie is a rewards API",
)

app.include_router(main_router)
