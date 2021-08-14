"""
Simple FastAPI application, running on port 8080
"""
from socket import gethostname
from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    """Check container"""
    return {"hostname": gethostname(),
            "timestamp": datetime.now(),
            "uuid": uuid4()}

@app.get("/isalive")
async def liveness_probe():
    """Smoke test ep"""
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
