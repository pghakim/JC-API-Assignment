import requests
import json


def test_post():
    """Sends a POST request to add a new pet. Passes assert if request was successful and JSON response matches expected """
    headers = {'Content-type': 'application/json'}
    data = {
        "id": 133000,
        "category": {
            "id": 133000,
            "name": "Freddie"
        },
        "name": "Freddie",
        "photoUrls": [
            "url"
        ],
        "tags": [
            {
                "id": 133000,
                "name": "Freddie"
            }
        ],
        "status": "available"
    }
    json_data = json.dumps(data)

    response = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, data=json_data)

    # Print the response content and assert response code and data
    print("Response Content for POST: ", response.content)
    print("Response Status Code: ", response.status_code)
    assert response.status_code == 200

    response_data = json.loads(response.content)
    assert response_data["name"] == "Freddie"
    assert response_data["photoUrls"] == ["url"]
    assert response_data["tags"] == [{"id": 133000, "name": "Freddie"}]
    assert response_data["status"] == "available"


def test_get():
    """Sends a GET request to return the pet with id 5. Passes assert if request was successful and JSON response matches expected"""

    response = requests.get("https://petstore.swagger.io/v2/pet/133000")

    # Print the response content and assert response code and data
    print("Response Content for GET: ", response.content)
    print("Response Status Code: ", response.status_code)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == "Freddie"
    assert response_data["photoUrls"] == ["url"]
    assert response_data["tags"] == [{"id": 133000, "name": "Freddie"}]
    assert response_data["status"] == "available"



def test_put():
    """Sends a PUT request to update a pet. Passes assert if request was successful and JSON response matches expected """
    headers = {'Content-type': 'application/json'}
    data = {
        "id": 133000,
        "category": {
            "id": 133000,
            "name": "Freddie"
        },
        "name": "Freddie",
        "photoUrls": [
            "urltwo"
        ],
        "tags": [
            {
                "id": 133000,
                "name": "Freddie"
            }
        ],
        "status": "sold"
    }
    json_data = json.dumps(data)
    response = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, data=json_data)

    # Print the response content and assert response code and data
    print("Response Content for PUT: ", response.content)
    print("Response Status Code: ", response.status_code)

    response_data = json.loads(response.content)
    assert response.status_code == 200
    assert response_data["name"] == "Freddie"
    assert response_data["photoUrls"] == ["urltwo"]
    assert response_data["tags"] == [{"id": 133000, "name": "Freddie"}]
    assert response_data["status"] == "sold"


def test_delete():
    """Sends a DELETE request to delete a pet. Passes assert if request was successful and JSON response matches expected """
    response = requests.delete("https://petstore.swagger.io/v2/pet/133000")

    # Print the response content and assert response code and data
    print("Response Content for DELETE: ", response.content)
    print("Response Status Code: ", response.status_code)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["type"] == "unknown"
    assert response_data["message"] == "133000"


test_post()
test_get()
test_put()
test_delete()
