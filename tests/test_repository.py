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


def test_record_click_returns_url_and_counts_click(db: sqlite3.Connection) -> None:
    repository = LinkRepository(db)
    repository.add("abc1234", "https://example.com")

    assert repository.record_click("abc1234") == "https://example.com"
    assert repository.get_stats("abc1234") == ("https://example.com", 1)


def test_record_click_returns_none_for_unknown_code(db: sqlite3.Connection) -> None:
    assert LinkRepository(db).record_click("missing") is None


def test_get_stats_starts_at_zero_clicks(db: sqlite3.Connection) -> None:
    repository = LinkRepository(db)
    repository.add("abc1234", "https://example.com")

    assert repository.get_stats("abc1234") == ("https://example.com", 0)


def test_get_stats_returns_none_for_unknown_code(db: sqlite3.Connection) -> None:
    assert LinkRepository(db).get_stats("missing") is None
