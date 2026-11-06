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
