from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
