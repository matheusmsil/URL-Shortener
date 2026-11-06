from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="URL Shortener")
app.include_router(router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
