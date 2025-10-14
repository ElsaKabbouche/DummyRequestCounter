from fastapi import FastAPI
from redis import Redis, exceptions
import os

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    socket_connect_timeout=0.2,
    socket_timeout=0.2,
)


@app.get("/")
def hello():
    try:
        hits = redis.incr("hits")
    except exceptions.RedisError:
        hits = "unavailable"
    return f"Hello! This page has been visited {hits} times."


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT", "8000")))
