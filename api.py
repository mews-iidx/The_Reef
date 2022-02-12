from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


#クイズを返す
@app.get("/quiz")
async def quiz(request: Request):
    return {'quiz': 'このゲーム機は何？' ,'image_url': 'https://m.media-amazon.com/images/I/714ii4ssR4L._AC_SL1500_.jpg'}

#ジャンルと残り数を返す
@app.get("/genre")
async def genre(request: Request):
    return {'secret' : 10, 'games': 20, 'foods' : 10}

#ジャンルをPOSTすると抽選を行い景品/画像を返す
@app.post("/result")
async def result(request: Request):
    return {'result_name' : 'PS5', 'result_image': 'https://m.media-amazon.com/images/I/714ii4ssR4L._AC_SL1500_.jpg'}

