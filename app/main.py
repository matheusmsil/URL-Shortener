from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="URL Shortener")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# Included last: routes match in order, and the router's GET /{code} would
# otherwise also match /health.
app.include_router(router)
