from fastapi import status


def test_create_user(client):
    payload = {
        "first_name": "test",
        "last_name": "app",
        "email": "test@gmail.com",
        "password": "x8lkkls",
        "confirm_password": "x8lkkls",
    }

    response = client.post("/api/users/", json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "first_name": "test",
        "last_name": "app",
        "email": "test@gmail.com",
    }
