from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

class RequestBody(BaseModel):
    text_str: str 


app = FastAPI()


@app.post("/")
async def create_item(request_body: RequestBody):
    if request_body.text_str is None or request_body.text_str == '':
        return {"status":"failed", "data": []}
    else:
        result = np.random.uniform(low=0, high=10, size=(500,))
        return {"status":"success", "data": list(result)}
