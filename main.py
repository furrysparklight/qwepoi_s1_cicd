from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Math & String API")

class MathRequest(BaseModel):
    number: float

class StringRequest(BaseModel):
    text: str

@app.post("/math/double")
async def double_number(data: MathRequest):
    return {"result": data.number * 2}

@app.post("/string/uppercase")
async def to_uppercase(data: StringRequest):
    return {"result": data.text.upper()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
