import re

from fastapi.testclient import TestClient


def test_create_link_returns_code_and_url(client: TestClient) -> None:
    response = client.post("/links", json={"url": "https://example.com/page"})

    assert response.status_code == 201
    body = response.json()
    assert re.fullmatch(r"[A-Za-z0-9]{7}", body["code"])
    assert body["url"] == "https://example.com/page"


def test_create_link_normalizes_url(client: TestClient) -> None:
    response = client.post("/links", json={"url": "https://example.com"})

    assert response.json()["url"] == "https://example.com/"


def test_create_link_rejects_invalid_url(client: TestClient) -> None:
    response = client.post("/links", json={"url": "not a url"})

    assert response.status_code == 422


def test_redirect_sends_known_code_to_its_url(client: TestClient) -> None:
    code = client.post("/links", json={"url": "https://example.com/page"}).json()[
        "code"
    ]

    response = client.get(f"/{code}", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["location"] == "https://example.com/page"


def test_redirect_returns_404_for_unknown_code(client: TestClient) -> None:
    response = client.get("/missing", follow_redirects=False)

    assert response.status_code == 404


def test_health_is_not_treated_as_a_code(client: TestClient) -> None:
    assert client.get("/health").json() == {"status": "ok"}
