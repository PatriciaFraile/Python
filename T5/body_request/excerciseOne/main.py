from fastapi import FastAPI
from models import items as item

app = FastAPI()


@app.post('/items')
async def create_items(item:item):
    return item

    

