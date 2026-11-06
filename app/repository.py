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

    def record_click(self, code: str) -> str | None:
        # Incrementing in SQL keeps concurrent clicks from overwriting each other.
        with self._db:
            row = self._db.execute(
                "UPDATE links SET clicks = clicks + 1 WHERE code = ? RETURNING url",
                (code,),
            ).fetchone()
        return None if row is None else str(row[0])

    def get_stats(self, code: str) -> tuple[str, int] | None:
        row = self._db.execute(
            "SELECT url, clicks FROM links WHERE code = ?", (code,)
        ).fetchone()
        return None if row is None else (str(row[0]), int(row[1]))
