import requests
import time
import allure

@allure.feature("CRUD Pets")
@allure.story("Update Pet")
@allure.description("Este test verifica la actualización de una mascota")

def test_update_pet(base_url, pet_payload):
    # Create pet
    create_response = requests.post(f"{base_url}/pet", json=pet_payload)
    assert create_response.status_code == 200, "Error al crear la mascota"
    pet_id = create_response.json()["id"]

    # Update fields 
    updated_payload = pet_payload.copy()
    updated_payload["id"] = pet_id
    updated_payload["name"] = "toby-updated"
    updated_payload["status"] = "pending"

    # Retry PUT + GET validation
    for _ in range(3):
        update_response = requests.put(f"{base_url}/pet", json=updated_payload)
        assert update_response.status_code == 200, "Error al actualizar la mascota"
        time.sleep(1)

        get_response = requests.get(f"{base_url}/pet/{pet_id}")
        if get_response.status_code == 200:
            data = get_response.json()
            if data["name"] == updated_payload["name"] and data["status"] == updated_payload["status"]:
                break
        time.sleep(1)

    # Final assertions
    assert get_response.status_code == 200, "Error al consultar la mascota actualizada"
    assert data["name"] == updated_payload["name"], "El nombre no se actualizó correctamente"
    assert data["status"] == updated_payload["status"], "El status no se actualizó correctamente"
