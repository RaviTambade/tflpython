# Python API Testing with FastAPI

## A Transflower mentor's introduction

When we build an API, we need to verify more than whether the application starts. We need evidence that each endpoint accepts valid requests, applies the right rules, and returns the expected status code and data.

In this lesson, we will test a small Product Catalog API. We will use `pytest` to run the tests and FastAPI's `TestClient` to send requests to the application without starting a separate web server.

## 1. The API testing toolkit

| Tool | Responsibility |
| --- | --- |
| FastAPI | Defines routes, request validation, and responses. |
| pytest | Discovers and runs tests, provides fixtures, and reports failures. |
| Starlette | The ASGI framework underneath FastAPI. |
| `TestClient` | A convenient synchronous client exposed by FastAPI and implemented by Starlette using HTTPX client functionality. |
| HTTPX | An HTTP client library. It can send real network requests or, through an ASGI transport, in-process requests. |
| Uvicorn | Runs an ASGI application as a web server. It is not needed for these in-process tests. |

Install the packages:

```text
python -m pip install fastapi httpx pytest
```

FastAPI depends on Starlette. Import `TestClient` from `fastapi.testclient`; you normally do not need to construct or subclass Starlette's client yourself.

## 2. How an in-process API test works

The test sends an HTTP-shaped request to the ASGI application through a test transport. The request is processed by the application, and the client receives a response object to inspect.

```text
pytest test
    |
    v
TestClient request
    |
    v
FastAPI / Starlette application
    |
    +--> routing and request validation
    +--> dependencies, middleware, and endpoint logic
    +--> response serialization
    |
    v
TestClient response --> pytest assertions
```

No TCP connection or separately running Uvicorn server is involved. These tests can exercise application behavior, but they do not verify DNS, networking, reverse proxies, server configuration, or the deployed environment. Those concerns need separate integration or end-to-end tests.

## 3. Build a small API

Create `main.py`. The app factory creates a fresh in-memory product catalog each time it is called. This makes it easy for every test to start with predictable data.

```python
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


class ProductInput(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


class Product(ProductInput):
    id: int


def create_app() -> FastAPI:
    app = FastAPI(title="Transflower Product Catalog")
    app.state.products = {
        1: Product(id=1, name="Laptop", price=1200.00),
        2: Product(id=2, name="Keyboard", price=75.00),
    }
    app.state.next_product_id = 3

    @app.get("/products", response_model=list[Product])
    def list_products() -> list[Product]:
        return list(app.state.products.values())

    @app.get("/products/{product_id}", response_model=Product)
    def get_product(product_id: int) -> Product:
        product = app.state.products.get(product_id)
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )
        return product

    @app.post(
        "/products",
        response_model=Product,
        status_code=status.HTTP_201_CREATED,
    )
    def create_product(product_input: ProductInput) -> Product:
        product = Product(
            id=app.state.next_product_id,
            **product_input.model_dump(),
        )
        app.state.products[product.id] = product
        app.state.next_product_id += 1
        return product

    @app.put("/products/{product_id}", response_model=Product)
    def update_product(
        product_id: int,
        product_input: ProductInput,
    ) -> Product:
        if product_id not in app.state.products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        product = Product(id=product_id, **product_input.model_dump())
        app.state.products[product_id] = product
        return product

    @app.delete(
        "/products/{product_id}",
        status_code=status.HTTP_204_NO_CONTENT,
    )
    def delete_product(product_id: int) -> Response:
        if product_id not in app.state.products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        del app.state.products[product_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


app = create_app()
```

The routes demonstrate common API behaviors:

| Request | Expected behavior |
| --- | --- |
| `GET /products` | Return the product list with `200 OK`. |
| `GET /products/1` | Return the laptop with `200 OK`. |
| `GET /products/99` | Return `404 Not Found`. |
| `POST /products` | Validate the body and create a product with `201 Created`. |
| `PUT /products/1` | Replace the product data with `200 OK`. |
| `DELETE /products/1` | Delete the product with `204 No Content`. |

This is a teaching example: the data is held in memory and disappears when the process ends. A real application would usually use a database or repository layer.

## 4. Write the tests

Create `test_main.py` beside `main.py`:

```python
import pytest
from fastapi.testclient import TestClient

from main import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as test_client:
        yield test_client


def test_list_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Laptop"


def test_get_product(client):
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Laptop",
        "price": 1200.0,
    }


def test_missing_product_returns_404(client):
    response = client.get("/products/99")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_create_product(client):
    response = client.post(
        "/products",
        json={"name": "Mouse", "price": 25.50},
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 3,
        "name": "Mouse",
        "price": 25.5,
    }


def test_invalid_product_is_rejected(client):
    response = client.post(
        "/products",
        json={"name": "Mouse", "price": -1},
    )

    assert response.status_code == 422


def test_update_product(client):
    response = client.put(
        "/products/1",
        json={"name": "Travel Laptop", "price": 950},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Travel Laptop"


def test_delete_product(client):
    response = client.delete("/products/1")

    assert response.status_code == 204
    assert response.content == b""
    assert client.get("/products/1").status_code == 404
```

Run the tests from the directory containing the files:

```text
python -m pytest -v
```

The `client` fixture gives each test a newly created app and closes the client when the test finishes. This keeps changes to the in-memory catalog from leaking between tests. Using `TestClient` as a context manager also runs the application's lifespan startup and shutdown handlers when they are defined.

## 5. What should an API test assert?

Check the parts of the response that form the endpoint's contract:

```python
assert response.status_code == 200
assert response.json()["name"] == "Laptop"
assert response.headers["content-type"].startswith("application/json")
```

For a useful test suite, cover:

1. **Success cases** — expected results for valid requests.
2. **Status codes** — for example, `200`, `201`, `204`, `404`, and `422`.
3. **Response body and headers** — returned fields, values, and content type.
4. **Validation and negative cases** — invalid types, missing fields, and invalid values.
5. **Business rules** — behavior such as updating and deleting records.
6. **Isolation** — each test should control its own data and not depend on test order.

Prefer assertions on meaningful behavior rather than implementation details. If a test fails, inspect `response.status_code`, `response.text`, and `response.headers` to understand what the API actually returned.

## 6. `TestClient` versus a live HTTP request

With `TestClient`, requests are sent to the application in-process:

```python
response = client.get("/products/1")
```

For a live request, the application must be running on a server, for example Uvicorn, and an HTTP client sends a URL over the network:

```python
import httpx

response = httpx.get("http://127.0.0.1:8000/products/1")
```

Use in-process tests for fast checks of routing, validation, dependencies, middleware, endpoint logic, and response serialization. Use live-server tests when you also need to verify the server, network path, deployment settings, or integration with external services.

For asynchronous tests, use HTTPX's `AsyncClient` with `ASGITransport` rather than calling the synchronous `TestClient` from an async test. Choose the client style that fits the application and test environment.

## 7. Mentor's learning path

| Stage | Practice |
| --- | --- |
| Beginner | `pytest`, `assert`, status codes, and `TestClient`. |
| Next | Test `GET`, `POST`, `PUT`, and `DELETE` endpoints. |
| Intermediate | Test validation errors, missing records, and response models. |
| Advanced | Use fixtures, dependency overrides, and controlled mocks. |
| Production-ready | Add database integration, authentication, test coverage, and CI checks. |

**Mentor's principle:** Building an endpoint shows that you can implement behavior. A clear test suite shows that you can verify and preserve that behavior as the application changes.

Start with the happy path, then test invalid inputs and missing resources. Keep each test independent, and add live integration tests when you need confidence in the network and deployment—not just the application code.
