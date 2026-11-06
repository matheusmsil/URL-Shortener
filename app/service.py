import secrets
import string
from collections.abc import Callable
from dataclasses import dataclass

from app.repository import CodeAlreadyExistsError, LinkRepository

ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7
MAX_ATTEMPTS = 5


@dataclass(frozen=True)
class Link:
    code: str
    url: str


@dataclass(frozen=True)
class LinkStats:
    code: str
    url: str
    clicks: int


class CodeGenerationError(Exception):
    pass


class LinkNotFoundError(Exception):
    pass


def generate_code() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


class LinkService:
    def __init__(
        self,
        repository: LinkRepository,
        code_generator: Callable[[], str] = generate_code,
    ) -> None:
        self._repository = repository
        self._code_generator = code_generator

    def create_link(self, url: str) -> Link:
        # Collisions are rare, so retry a few times instead of checking first.
        for _ in range(MAX_ATTEMPTS):
            code = self._code_generator()
            try:
                self._repository.add(code, url)
            except CodeAlreadyExistsError:
                continue
            return Link(code=code, url=url)
        raise CodeGenerationError(f"No free code after {MAX_ATTEMPTS} attempts")

    def resolve(self, code: str) -> str:
        """Return the URL for a code and count the visit as a click."""
        url = self._repository.record_click(code)
        if url is None:
            raise LinkNotFoundError(code)
        return url

    def get_stats(self, code: str) -> LinkStats:
        stats = self._repository.get_stats(code)
        if stats is None:
            raise LinkNotFoundError(code)
        url, clicks = stats
        return LinkStats(code=code, url=url, clicks=clicks)
