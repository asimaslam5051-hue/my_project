from fastapi.testclient import Testclient
from main import app


client = Testclient(app)

def test_get_all_blogs():
    response = client.get("blog/all?page=1")
    assert response.status_code == 200 
