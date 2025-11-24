from fastapi.testclient import Testclient
from main import app


client = Testclient(app)

def test_get_all_blogs():
    response = client.get("blog/all?page=1")
    assert response.status_code == 200

def test_auth_error():
    response= client.post("/token",
    data = {"username":"","password":""}
    )
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")[0].get("msg")
    assert message == "field required"
def test_auth_success():
     response= client.post("/token",
    data = {"username":"cat","password":"cat"}
     )
     access_token = response.json().get("access_token")
     assert access_token

def test_post_article():
    auth = client.post("/token",
    data = {"username":"","password":""}
    )
    access_token = auth.json().get("access_token")
    assert  access_token

    response = client.post(
        "/article/",
        {
            "title" : "Test article",
            "content" : "Test content",
            "published" : True,
            "creator_id" : 1
        },
        headers = {
            "Authorization":"bearer"+ access_token
        }
    )

    assert  response.status_code == 200
    assert response.jason().get("title") == "Test_article"