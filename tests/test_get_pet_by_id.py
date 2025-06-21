import requests
import time
import allure

@allure.feature("CRUD Pets")
@allure.story("Get Pet By Id")
@allure.description("Este test valida que se pueda consultar una mascota recién creada por su id")

def test_get_pet_by_id(base_url, pet_payload):
    # Create a pet
    create_response = requests.post(f"{base_url}/pet", json=pet_payload)
    assert create_response.status_code == 200, "No se pudo crear la mascota"
    pet_id = create_response.json()["id"]

    # Get pet by id + retry max 3 times (por si el recurso tarda)
    for _ in range(3):
        get_response = requests.get(f"{base_url}/pet/{pet_id}")
        if get_response.status_code == 200:
            break
        time.sleep(1)

    assert get_response.status_code == 200, f"Expected 200, got {get_response.status_code}"
    data = get_response.json()
    assert data["id"] == pet_id, "El ID no coincide con el creado"
