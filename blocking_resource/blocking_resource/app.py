import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/blocking-resource")
async def blocking_resource():
    await asyncio.sleep(5)
    return {"msg": "done!"}

