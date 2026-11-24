import json
from pathlib import Path
import pytest
from utils.api_client import APIS

@pytest.fixture(scope="module")
def api_client():
    return APIS()

def \
load_test_data():
    file_path = Path(__file__).parent.parent / "testdata" / "activity.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# GET
def test_get_authors(api_client):
    response = api_client.get("/Authors")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


# POST
def test_create_activity(api_client):
    test_data = load_test_data()
    payload = test_data["create_activity"]
    response = api_client.post("/Activities", payload)
    print(response.json())
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["completed"] == payload["completed"]


# PUT
def test_update_activity(api_client):
    test_data = load_test_data()
    payload = test_data["update_activity"]
    response = api_client.put("/Activities/151", payload)
    print(response.json())
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["completed"] == payload["completed"]

# DELETE
def test_delete_activity(api_client):
    response = api_client.delete("/Activities/225")
    print("Status Code:", response.status_code)
    assert response.status_code == 200