import os

import uvicorn

from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST_ADDRESS") or "0.0.0.0", port=int(os.getenv("HOST_PORT") or "8090"))
