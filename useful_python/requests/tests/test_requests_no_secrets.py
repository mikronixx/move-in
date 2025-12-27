import requests_mock
from useful_python.requests_v2 import requests_no_secrets as rns

def test_get_users_success():
    fake_users = [
        {"id": 1, "name": "Wilma"},
        {"id": 2, "name": "Betty"}
    ]
    with requests_mock.Mocker() as m:
        m.get(f"{rns.API_URL}users", json=fake_users)
        result = rns.get_users()
        assert result == {1: "Wilma", 2: "Betty"}

def test_get_users_failure():
    with requests_mock.Mocker() as m:
        m.get(f"{rns.API_URL}users", status_code=500)
        result = rns.get_users()
        assert result == {}

def test_get_post_counts_by_user():
    fake_users = [
        {"id": 1, "name": "Wilma"},
        {"id": 2, "name": "Betty"}
    ]
    fake_posts = [
        {"userId": 1, "id": 101, "title": "Post 1"},
        {"userId": 1, "id": 102, "title": "Post 2"},
        {"userId": 2, "id": 103, "title": "Post 3"}
    ]
    with requests_mock.Mocker() as m:
        m.get(f"{rns.API_URL}users", json=fake_users)
        m.get(f"{rns.API_URL}posts", json=fake_posts)
        result = rns.get_post_counts_by_user()
        expected = [
            {"user": "Wilma", "postcount": 2},
            {"user": "Betty", "postcount": 1}
        ]
        assert result == expected