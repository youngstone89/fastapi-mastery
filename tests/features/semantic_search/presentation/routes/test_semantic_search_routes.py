import pytest
from app.features.semantic_search.presentation.routes.semantic_search_routes import \
    router
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Assuming your router is located in a module named "app.routers"


# Create a FastAPI app and include the router
app = FastAPI()
app.include_router(router)


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_add_sentence(client, mocker):
    payload = {"text": "This is a test sentence"}
    mocker.patch(
            "app.features.semantic_search.application.usecases.semantic_search_usecase.SemanticSearchUseCase.add_sentence",
            return_value=None
        )
    response = client.post("/add-sentence", json=payload)
    print(response.json())  # This will print the response body

    assert response.status_code == 200
    assert response.json() == {"message": "Sentence added successfully"}


def test_async_find_intention(client, mocker):
    # Mock the SemanticSearchUseCase's async_find_intention method
    mocker.patch(
        "app.features.semantic_search.application.usecases.semantic_search_usecase.SemanticSearchUseCase.async_find_intention",
        return_value="Mocked Intention"
    )
    response = client.get("/async-find-intention",
                          params={"query": "test query"})
    assert response.status_code == 200
    assert response.json() == {"intention": "Mocked Intention"}


def test_sync_find_intention(client, mocker):
    # Mock the SemanticSearchUseCase's sync_find_intention method
    mocker.patch(
        "app.features.semantic_search.application.usecases.semantic_search_usecase.SemanticSearchUseCase.sync_find_intention",
        return_value="Mocked Intention"
    )
    response = client.get("/sync-find-intention",
                          params={"query": "test query"})
    assert response.status_code == 200
    assert response.json() == {"intention": "Mocked Intention"}


def test_read_async_item(client):
    response = client.get("/async/items/1", params={"q": "test"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "test"}


def test_read_sync_item(client):
    response = client.get("/sync/items/1", params={"q": "test"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "test"}
