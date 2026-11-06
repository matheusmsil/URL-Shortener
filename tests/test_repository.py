import sqlite3

import pytest

from app.repository import CodeAlreadyExistsError, LinkRepository


def test_add_stores_link(db: sqlite3.Connection) -> None:
    LinkRepository(db).add("abc1234", "https://example.com")

    row = db.execute("SELECT url FROM links WHERE code = ?", ("abc1234",)).fetchone()
    assert row == ("https://example.com",)


def test_add_rejects_duplicate_code(db: sqlite3.Connection) -> None:
    repository = LinkRepository(db)
    repository.add("abc1234", "https://example.com")

    with pytest.raises(CodeAlreadyExistsError):
        repository.add("abc1234", "https://other.example.com")


def test_get_url_returns_stored_url(db: sqlite3.Connection) -> None:
    repository = LinkRepository(db)
    repository.add("abc1234", "https://example.com")

    assert repository.get_url("abc1234") == "https://example.com"


def test_get_url_returns_none_for_unknown_code(db: sqlite3.Connection) -> None:
    assert LinkRepository(db).get_url("missing") is None
