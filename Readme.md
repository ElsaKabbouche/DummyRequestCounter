### 🗄️ Persistent Storage and Custom Network

- Redis now uses a volume `redis_data` to persist data between container restarts.
- Both `app` and `redis` are connected to a custom Docker network `dummy_network` for isolated and reliable communication.

To rebuild with these changes:
```bash
docker-compose down -v
docker-compose up --build# trigger workflow
