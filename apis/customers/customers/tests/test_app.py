from chalice.test import Client
from app import app
import json


def test_create_person():
    with Client(app) as client:
        response = client.http.post(
            "/customers/person",
            body=json.dumps({"name": "usuário4", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response)
        print(response.json_body)
        assert response.json_body["statusCode"] == 201


def test_update_person():
    with Client(app) as client:
        response = client.http.put(
            "/customers/person",
            body=json.dumps({"name": "usuário1", "phone": 47999999999}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_person():
    with Client(app) as client:
        response = client.http.delete(
            "/customers/person",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_persons():
    with Client(app) as client:
        response = client.http.get("/customers/persons")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_person():
    with Client(app) as client:
        response = client.http.get(f"/customers/person/usuario1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 404


def test_create_company():
    with Client(app) as client:
        response = client.http.post(
            "/customers/company",
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 201


def test_update_company():
    with Client(app) as client:
        response = client.http.put(
            "/customers/company",
            body=json.dumps({"name": "empresa1", "telefone": 47999999999}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 404


def test_delete_company():
    with Client(app) as client:
        response = client.http.delete(
            "/customers/company",
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 404


def test_get_companies():
    with Client(app) as client:
        response = client.http.get("/customers/companies")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_company():
    with Client(app) as client:
        response = client.http.get("/customers/company/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 404
