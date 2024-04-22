from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Datas(BaseModel):
    id: Optional[int] = None
    title:str
    description:str

datas=[
    {
        "id":1,
        "Title": "What is Lorem Ipsum?",
        "Description":"is simply dummy text of the printing and typesetting industry."
    },
    {
        "id":2,
        "Title":"Why do we use it?",
        "Description":"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
    }
]

@app.get("/", tags=['Home'])
def home():
    return "Hello World"
@app.get("/home", tags=['Home'])
def home():
    return HTMLResponse('<h1>Hello World</h1>')
@app.get("/datas", tags=['Home'])
def home():
    return datas
@app.get("/datas/{id}", tags=['Home'])
def home(id:int):
    for data in datas:
        if data['id']==id:
            return data
    return[]
@app.post("/add", tags=['Append'])
def append_data(data:Datas):
    datas.append(data.model_dump())
@app.put("/data/{id}", tags=['Update'])
def put_data(id:int,data:Datas):
    for d in datas:
        if d['id']==id:
            d['Title'] = data.title
            d['Description'] = data.description
    return datas

@app.delete("/data/{id}", tags=['Delete'])
def delete_data(id:int):
     for data in datas:
        if data['id']==id:
            datas.remove(data)
     return datas
