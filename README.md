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

---

## apiサーバ起動

```bash
docker-compose up -d --build

# migration
docker-compose exec api poetry run python -m app.migrate_db
```

### Swagger API Docs

APIサーバ起動後
http://localhost:8000/docs

### 問題と景品追加

1. reef.present_categories にプレゼントジャンルを追加
2. reef.presents にプレゼントを追加. is_usedはすべて0
3. reef.quizzes に問題追加. order_numberは使ってないのでidと同じ数字. is_usedはすべて0

---


testtest
