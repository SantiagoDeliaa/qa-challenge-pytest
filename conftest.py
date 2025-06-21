import pytest
import random

@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def pet_payload():
    random_id = random.randint(100000, 999999)
    return {
        "id": random_id,
        "category": {
            "id": 1,
            "name": "dog"
        },
        "name": "test_toby",
        "photoUrls": ["testPhoto"],
        "tags": [
            {
                "id": 1,
                "name": "big_dog"
            }
        ],
        "status": "available"
    }
