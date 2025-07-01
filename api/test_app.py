

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_products(client):
    res = client.get("/products")
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert len(res.json) == 2

def test_place_order_success(client):
    res = client.post("/order", json={"product_id": 1, "quantity": 2})
    assert res.status_code == 200
    assert res.json["total"] == 40

def test_place_order_product_not_found(client):
    res = client.post("/order", json={"product_id": 999})
    assert res.status_code == 404
