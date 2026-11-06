import re
import sqlite3

import pytest

from app.repository import LinkRepository
from app.service import (
    CodeGenerationError,
    LinkNotFoundError,
    LinkService,
    generate_code,
)


def test_generate_code_returns_seven_base62_characters() -> None:
    assert re.fullmatch(r"[A-Za-z0-9]{7}", generate_code())


def test_create_link_saves_link(db: sqlite3.Connection) -> None:
    link = LinkService(LinkRepository(db)).create_link("https://example.com")

    assert link.url == "https://example.com"
    row = db.execute("SELECT url FROM links WHERE code = ?", (link.code,)).fetchone()
    assert row == ("https://example.com",)


def test_create_link_retries_when_code_is_taken(db: sqlite3.Connection) -> None:
    repository = LinkRepository(db)
    repository.add("taken00", "https://other.example.com")
    codes = iter(["taken00", "free000"])
    service = LinkService(repository, code_generator=lambda: next(codes))

    link = service.create_link("https://example.com")

    assert link.code == "free000"


def test_create_link_gives_up_when_every_code_is_taken(
    db: sqlite3.Connection,
) -> None:
    repository = LinkRepository(db)
    repository.add("taken00", "https://other.example.com")
    service = LinkService(repository, code_generator=lambda: "taken00")

    with pytest.raises(CodeGenerationError):
        service.create_link("https://example.com")


def test_get_url_returns_url_for_known_code(db: sqlite3.Connection) -> None:
    service = LinkService(LinkRepository(db))
    link = service.create_link("https://example.com")

    assert service.get_url(link.code) == "https://example.com"


def test_get_url_raises_for_unknown_code(db: sqlite3.Connection) -> None:
    with pytest.raises(LinkNotFoundError):
        LinkService(LinkRepository(db)).get_url("missing")
