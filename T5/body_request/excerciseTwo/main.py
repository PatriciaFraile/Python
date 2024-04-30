from fastapi import FastAPI
from endpoints import items 

app = FastAPI(docs_url="/items/docs", redoc_url=None,openapi_url="/items/openapi.json")

app.include_router(items.router)