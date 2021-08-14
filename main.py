"""
Simple FastAPI application, running on port 8080
"""
import os
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


@app.get("/isalive", status_code=status.HTTP_200_OK)
async def liveness_probe():
    """Smoke test ep"""
    return {"status": "OK"}


# if __name__ == "__main__":
#     port = os.environ.get('PORT', 8080)
#     uvicorn.run(app, host="0.0.0.0", port=port)
