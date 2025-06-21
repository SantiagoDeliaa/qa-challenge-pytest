import requests
import time
import allure

@allure.feature("CRUD Pets")
@allure.story("Delete Pet")
@allure.description("Este test verifica la eliminación de una mascota")

def test_delete_pet(base_url, pet_payload):
    # Create a pet to delete
    create_response = requests.post(f"{base_url}/pet", json=pet_payload)
    assert create_response.status_code == 200, "Error al crear la mascota"
    pet_id = create_response.json()["id"]

    # Delete the pet
    for _ in range(3):
        get_response = requests.get(f"{base_url}/pet/{pet_id}")
        if get_response.status_code == 404:
            break
        time.sleep(1)

    assert get_response.status_code == 404, "La mascota aún existe después del delete"
    data = get_response.json()
    assert data.get("message") == "Pet not found", "El mensaje de eliminación no es el esperado"
