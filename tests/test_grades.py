def get_token(client):
    response = client.post("/auth/login", json={
        "username": "teacher1",
        "password": "admin123"
    })
    return response.json()["access_token"]


def test_add_marks(client):
    token = get_token(client)

    response = client.post(
        "/grades/",
        json={
            "name": "Test Student",
            "student_class": "10A",
            "subject_marks": {
                "math": 90,
                "science": 80
            }
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_add_marks_unauthorized(client):
    response = client.post(
        "/grades/",
        json={
            "name": "Unauthorized",
            "student_class": "10A",
            "subject_marks": {"math": 90}
        }
    )

    assert response.status_code == 401


def test_invalid_marks(client):
    token = get_token(client)

    response = client.post(
        "/grades/",
        json={
            "name": "Bad Data",
            "student_class": "10A",
            "subject_marks": {"math": 150}
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422


def test_get_grades(client):
    token = get_token(client)

    response = client.get(
        "/grades/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200