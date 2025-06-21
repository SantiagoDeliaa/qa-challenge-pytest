import requests
import allure

@allure.feature("CRUD Pets")
@allure.story("Add Pet")
@allure.description("Este test verifica la creación de una mascota")

def test_add_pet(base_url, pet_payload):
    url = f"{base_url}/pet"
    response = requests.post(url, json=pet_payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert data["name"] == pet_payload["name"], "Name mismatch"
    assert data["status"] == pet_payload["status"], "Status mismatch"
    assert data["tags"][0]["name"] == pet_payload["tags"][0]["name"], "Tag mismatch"
    assert isinstance(data["id"], int), "ID is not an integer"