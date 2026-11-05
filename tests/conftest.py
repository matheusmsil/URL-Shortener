import sqlite3
from collections.abc import Iterator
from pathlib import Path

import pytest

from app.db import connect


@pytest.fixture
def db(tmp_path: Path) -> Iterator[sqlite3.Connection]:
    connection = connect(tmp_path / "test.db")
    yield connection
    connection.close()
