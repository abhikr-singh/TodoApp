from fastapi import status
from ..routers.admin import get_db, get_current_user
from .utils import test_todo, client, override_get_current_user, override_get_db, app

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "complete": False,
            "title": "Test Todo",
            "description": "Test Description",
            "id": 1,
            "priority": 1,
            "owner_id": 1,
        }
    ]
