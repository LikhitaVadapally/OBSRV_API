# tests/test_dataset_api.py
import pytest
from httpx import AsyncClient
from app.main import app
import asyncio

@pytest.mark.asyncio
async def test_create_read_update_delete():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create
        payload = {
            "id": "test-id-1",
            "dataset_id": "test-id-1",
            "type": "dataset",
            "name": "Test Dataset"
        }
        response = await ac.post("/v1/datasets", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "test-id-1"

        # Read
        response = await ac.get(f"/v1/datasets/{payload['id']}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Test Dataset"

        # Update
        update_payload = {"name": "Updated Dataset"}
        response = await ac.patch(f"/v1/datasets/{payload['id']}", json=update_payload)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated Dataset"

        # Delete
        response = await ac.delete(f"/v1/datasets/{payload['id']}")
        assert response.status_code == 204

        # Confirm deletion
        response = await ac.get(f"/v1/datasets/{payload['id']}")
        assert response.status_code == 404