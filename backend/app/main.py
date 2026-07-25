from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI Data Analysis Platform"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Prism",
        "environment": settings.ENVIRONMENT
    }


@app.get("/health")
def health_check():
    return {
        "status": "Prism is running"
    }