import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


API_ENDPOINT = "http://api:8000"

app.mount("/static", StaticFiles(directory="static"), name="static")


def linebreaksbr(arg):
    return arg.replace("\r\n", "<br>")


templates.env.filters["linebreaksbr"] = linebreaksbr


@app.get("/")
async def route_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/quiz")
async def quiz(request: Request):
    ret = requests.get(API_ENDPOINT + "/quiz")

    j = ret.json()

    if not j['is_enable']:
        return templates.TemplateResponse("end.html", {"request": request})
    print('is_enable', j['is_enable'])

    ans_ret = requests.get(API_ENDPOINT + "/answer", params={"quiz_id": j["quiz_id"]})

    answer = ans_ret.json()["answer"]
    j["answer"] = answer
    if j["image_url"] is None:
        return templates.TemplateResponse("quiz.html", {"request": request, "ret": j})
    else:
        return templates.TemplateResponse(
            "quiz_with_image.html", {"request": request, "ret": j}
        )
    # return templates.TemplateResponse("quiz.html", {'request': request, 'quiz': ret.json()['quiz']})


@app.get("/random")
async def read_item(request: Request):
    ret = requests.get(API_ENDPOINT + "/genre")

    # TODO: エラーハンドリングしたほうがよい
    if ret is None:
        return templates.TemplateResponse("index.html", {"request": request})
    j = ret.json()

    return templates.TemplateResponse("random.html", {"request": request, "genres": j})


@app.get("/result/{result_genre}")
async def read_item(request: Request, result_genre: str):
    ret = requests.get(API_ENDPOINT + "/result/" + result_genre)
    if ret is None:
        return templates.TemplateResponse("index.html", {"request": request})
    j = ret.json()
    print(j)
    return templates.TemplateResponse("result.html", {"request": request, "ret": j})
