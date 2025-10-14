from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import app as app_module

client = TestClient(app_module.app)


def test_root():
    mock_redis = MagicMock()
    mock_redis.incr.return_value = 1
    mock_redis.get.return_value = b"1"

    original = app_module.redis
    try:
        app_module.redis = mock_redis
        resp = client.get("/")
        assert resp.status_code == 200
        assert "Hello!" in resp.text
    finally:
        app_module.redis = original
