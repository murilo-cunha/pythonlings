from fastapi3 import client


def test_list_all():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_filter_by_category():
    fruits = client.get("/items/?category=fruit").json()
    assert len(fruits) == 2
    assert all(f["category"] == "fruit" for f in fruits)

def test_filter_vegetable():
    veggies = client.get("/items/?category=vegetable").json()
    assert len(veggies) == 1
    assert veggies[0]["name"] == "Carrot"
