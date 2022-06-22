from flask import Flask
import httpx

app = Flask(__name__)


def get_resource() -> dict:
    r = httpx.get("http://localhost:8000/blocking-resource", timeout=10.0)
    return r.json()


@app.get("/resource")
def resource():
    return get_resource()

