import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        log_level="info",
        host="127.0.0.1",
        reload=True,
        debug=True,
    )
    # $ uvicorn example:app --port 5000 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem
