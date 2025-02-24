from .utils import (
    TestingSessionLocal,
    client,
    override_get_db,
    override_get_current_user,
    app,
    test_user,
)
from ..routers.users import get_db, get_current_user
from fastapi import status
from ..models import Users

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@email.com"
    assert response.json()["first_name"] == "test"
    assert response.json()["last_name"] == "user"
    assert response.json()["role"] == "admin"
    assert response.json()["role"] == "admin"


def test_change_password_success(test_user):
    response = client.put(
        "/user/password",
        json={"password": "testpassword", "new_password": "newpassword"},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_passowrd(test_user):
    response = client.put(
        "/user/password",
        json={"password": "testpassword1", "new_password": "newpassword"},
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/2222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
