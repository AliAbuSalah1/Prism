from fastapi import FastAPI

app = FastAPI(
    title="Prism API",
    description="AI Data Analysis Platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Prism",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Prism is running"
    }