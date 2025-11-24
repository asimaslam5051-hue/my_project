from fastapi.testclient import Testclient
from main import app


client = Testclient(app)

def test_get_all_blogs():
    