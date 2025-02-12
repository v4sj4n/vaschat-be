from fastapi import FastAPI
import uvicorn
from routes.completion import completion_router


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "VasChat is running!"}


app.include_router(completion_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=4444, reload=True)
