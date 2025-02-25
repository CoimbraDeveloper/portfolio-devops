import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_client():
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Welcome, I'm Diego Coimbra!"