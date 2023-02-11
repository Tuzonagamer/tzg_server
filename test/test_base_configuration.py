
from . import app , client 



def test_request_example(client):
    response = client.get("/")
    assert b"service" in response.data
    assert response.status_code == 200