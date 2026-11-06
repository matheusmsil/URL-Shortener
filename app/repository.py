import sqlite3


class CodeAlreadyExistsError(Exception):
    pass


class LinkRepository:
    def __init__(self, db: sqlite3.Connection) -> None:
        self._db = db

    def add(self, code: str, url: str) -> None:
        try:
            with self._db:
                self._db.execute(
                    "INSERT INTO links (code, url) VALUES (?, ?)", (code, url)
                )
        except sqlite3.IntegrityError as error:
            raise CodeAlreadyExistsError(code) from error
