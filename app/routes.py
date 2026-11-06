import sqlite3
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

from app.db import get_db
from app.repository import LinkRepository
from app.service import LinkNotFoundError, LinkService

router = APIRouter()


class CreateLinkRequest(BaseModel):
    url: HttpUrl


class LinkResponse(BaseModel):
    code: str
    url: str


class StatsResponse(BaseModel):
    code: str
    url: str
    clicks: int


def get_service(db: Annotated[sqlite3.Connection, Depends(get_db)]) -> LinkService:
    return LinkService(LinkRepository(db))


@router.post("/links", status_code=status.HTTP_201_CREATED)
def create_link(
    request: CreateLinkRequest,
    service: Annotated[LinkService, Depends(get_service)],
) -> LinkResponse:
    link = service.create_link(str(request.url))
    return LinkResponse(code=link.code, url=link.url)


@router.get("/links/{code}/stats")
def get_stats(
    code: str,
    service: Annotated[LinkService, Depends(get_service)],
) -> StatsResponse:
    try:
        stats = service.get_stats(code)
    except LinkNotFoundError as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Link not found") from error
    return StatsResponse(code=stats.code, url=stats.url, clicks=stats.clicks)


# 302, not 301: browsers cache a 301 and stop calling the server, so clicks
# could no longer be counted.
@router.get("/{code}")
def redirect(
    code: str,
    service: Annotated[LinkService, Depends(get_service)],
) -> RedirectResponse:
    try:
        url = service.resolve(code)
    except LinkNotFoundError as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Link not found") from error
    return RedirectResponse(url, status_code=status.HTTP_302_FOUND)
