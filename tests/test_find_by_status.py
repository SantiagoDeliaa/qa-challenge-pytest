import requests

def test_find_by_status(base_url):
    status = "pending"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})
    
    assert response.status_code == 200, "La solicitud no fue exitosa"
    pets = response.json()

    for pet in pets:
        assert pet["status"] == status, f"Se encontró un pet con status distinto: {pet['status']}"
