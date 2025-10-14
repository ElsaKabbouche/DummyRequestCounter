# tests/test_app.py
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app import app

client = TestClient(app)

def test_root():
    # Create a mock Redis client
    mock_redis = MagicMock()
    mock_redis.incr.return_value = None
    mock_redis.get.return_value = b"1"

    # Override the Redis client in the app
    app.redis = mock_redis

    # Call the endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello!" in response.text