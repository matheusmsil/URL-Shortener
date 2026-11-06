import sqlite3
from typing import Annotated

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, HttpUrl

from app.db import get_db
from app.repository import LinkRepository
from app.service import LinkService

router = APIRouter()


class CreateLinkRequest(BaseModel):
    url: HttpUrl


class LinkResponse(BaseModel):
    code: str
    url: str


def get_service(db: Annotated[sqlite3.Connection, Depends(get_db)]) -> LinkService:
    return LinkService(LinkRepository(db))


@router.post("/links", status_code=status.HTTP_201_CREATED)
def create_link(
    request: CreateLinkRequest,
    service: Annotated[LinkService, Depends(get_service)],
) -> LinkResponse:
    link = service.create_link(str(request.url))
    return LinkResponse(code=link.code, url=link.url)
