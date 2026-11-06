import os
import sqlite3
from collections.abc import Iterator
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS links (
    code TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0
)
"""


def connect(path: str | Path) -> sqlite3.Connection:
    # FastAPI may run a dependency and its endpoint in different threads,
    # so the connection must not be tied to the thread that created it.
    connection = sqlite3.connect(path, check_same_thread=False)
    connection.execute(SCHEMA)
    return connection


def get_db() -> Iterator[sqlite3.Connection]:
    connection = connect(os.environ.get("DATABASE_PATH", "links.db"))
    try:
        yield connection
    finally:
        connection.close()
