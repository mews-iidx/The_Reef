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

    l = [
        {'quiz': '社内の喫煙者は何人？' ,'image_url': None },
        {'quiz': 'このゲーム機は何？' ,'image_url': 'https://m.media-amazon.com/images/I/714ii4ssR4L._AC_SL1500_.jpg'       }
        ]
    
    import random
    random.shuffle(l)



    return l[0]

#ジャンルと残り数を返す
@app.get("/genre")
async def genre(request: Request):

    return {'genres' : [
        {'genre_name': 'secret', 'genre_count': 10},
        {'genre_name': 'game', 'genre_count': 8},
        {'genre_name': 'other', 'genre_count': 6},
    ]}

#ジャンルをPOSTすると抽選を行い景品/画像を返す
@app.get("/result/{genre_name}")
async def result(request: Request, genre_name: str):
    print(genre_name)
    return {'result_name' : 'PS5', 'result_image': 'https://m.media-amazon.com/images/I/714ii4ssR4L._AC_SL1500_.jpg'}

