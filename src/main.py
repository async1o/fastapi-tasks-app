from fastapi import FastAPI

from src.api.main_router import main_router
from src.databases.database import lifespan

import logging



logging.basicConfig(level=logging.INFO)


app = FastAPI(lifespan=lifespan)

app.include_router(main_router)
