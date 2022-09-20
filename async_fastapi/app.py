from fastapi import FastAPI
import httpx

app = FastAPI()


async def get_resource() -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.get("http://localhost:8000/blocking-resource", timeout=10.0)
        return r.json()


@app.get("/resource")
async def resource():
    return await get_resource()

