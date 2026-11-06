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
