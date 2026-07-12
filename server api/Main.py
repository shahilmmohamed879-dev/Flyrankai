from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/status")
def read_status():
    return {"status": "ok", "service": "mini-backend"}
