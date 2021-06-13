from fastapi import FastAPI
from database import engine
from router import router
import uvicorn

app = FastAPI()

#models.Base.metadata.create_all(engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)