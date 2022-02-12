# readme

1. フロントコードとバックエンドコードを無造作に詰める
1. あとで整理
1. Docker化



## requirements

* ubuntu 20.04でテスト
* python3.8.10


## 準備

```bash
python3 -m venv
source venv/bin/activate
pip install -r requirements.txt

```

## frontサーバ起動

```bash
uvicorn main:app --reload
```

## apiサーバ起動

```bash
uvicorn api:app --reload --port 8080
```

## メモ

## ワイヤーフレーム途中

* [draw.io](https://drive.google.com/file/d/10_TuLvSiAlLqwT481x0TwDVYuAvxnWMN/view?usp=sharing)
