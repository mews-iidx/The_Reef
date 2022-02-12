from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import requests

templates = Jinja2Templates(directory="templates")

app = FastAPI()


API_ENDPOINT ='http://localhost:8080'

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def route_index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


@app.get("/quiz")
async def quiz(request: Request):
    ret = requests.get(API_ENDPOINT + '/quiz')

    #TODO: エラーハンドリングしたほうがよい
    if ret is None:
        return templates.TemplateResponse("index.html", {'request': request})
    j = ret.json()
    return templates.TemplateResponse("quiz.html", {'request': request, 'ret': j})
    #return templates.TemplateResponse("quiz.html", {'request': request, 'quiz': ret.json()['quiz']})

@app.get("/random")
async def read_item(request: Request):
    return templates.TemplateResponse("random.html", {'request': request})

@app.get("/result")
async def read_item(request: Request):
    return templates.TemplateResponse("result.html", {'request': request})
