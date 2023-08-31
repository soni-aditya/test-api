from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

class RequestBody(BaseModel):
    text_str: str | None = ''


app = FastAPI()


@app.post("/")
async def create_item(request_body: RequestBody):
    result = np.random.uniform(low=0, high=10, size=(500,))
    return {"status":"success", "data": list(result)}
