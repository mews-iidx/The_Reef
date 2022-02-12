from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


@app.get("/quiz")
async def read_item(request: Request):
    return templates.TemplateResponse("quiz.html", {'request': request})

@app.get("/random")
async def read_item(request: Request):
    return templates.TemplateResponse("random.html", {'request': request})

@app.get("/result")
async def read_item(request: Request):
    return templates.TemplateResponse("result.html", {'request': request})
