from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_name_message():
    response = client.post("/name", json={"name": "John"})
    assert response.status_code == 200
    assert response.json() == {"message": "John, that is a great name."}

def test_get_name_message_empty():
    response = client.post("/name", json={"name": ""})
    assert response.status_code == 200
    assert response.json() == {"message": ", that is a great name."}
