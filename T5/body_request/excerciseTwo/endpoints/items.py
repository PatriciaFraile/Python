from fastapi import APIRouter
from services import search as crud
from pydantic import BaseModel
from typing import Optional,List


router = APIRouter()

class item (BaseModel):
    query:Optional[str]= None
    page:Optional[int] = None
    page_size:Optional[int]= None

@router.post("/search/")
async def search_items(params: item):
    results=[]
    for i in crud.load_data():
        if(params.query is None or params.query.lower() in i["query"].lower() and params.page is None or params.page.lower()
            in i["page"].lower() and params.page_size is None or params.page_size.lower() in i["page_size"].lower() ):
            results.append(i)
    return {"results": results}


# filtros Date,Name
# data->{filter_query_page_page_size:{product data}}


