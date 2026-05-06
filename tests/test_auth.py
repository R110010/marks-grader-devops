def test_login_success(client):
    response = client.post("/auth/login", json={
        "username": "teacher1",
        "password": "admin123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_failure(client):
    response = client.post("/auth/login", json={
        "username": "teacher1",
        "password": "wrongpass"
    })

    assert response.status_code == 401