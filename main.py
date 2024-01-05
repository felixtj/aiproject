from fastapi import FastAPI

app = FastAPI()

print ("masuk")

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI 8!"}