from fastapi import FastAPI

app = FastAPI(
    title="IT Ticket Management API",
    description="A REST API for creating and managing IT support tickets.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "IT Ticket Management API is running"}