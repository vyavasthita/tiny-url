from fastapi import FastAPI
import uvicorn
from src.router.shortner_router import shortner_router


app = FastAPI()

app.include_router(shortner_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
