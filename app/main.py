from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/im_ok")
async def health():
    return {"status": "ok"}
    
Instrumentator().instrument(app).expose(app)

