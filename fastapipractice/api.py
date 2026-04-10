from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def get_items():
    return [{"name": "item"}

    ]
