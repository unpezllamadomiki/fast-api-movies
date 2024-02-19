from contextlib import asynccontextmanager
from typing import Any

import uvicorn
from fastapi import FastAPI

from src.shared.infrastructure.database_mapper import SLQAlchemyMapper


@asynccontextmanager
async def lifespan(_: FastAPI) -> Any:
    SLQAlchemyMapper()
    yield

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)