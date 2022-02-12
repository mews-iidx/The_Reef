import os

from sqlalchemy import create_engine

from app.models.present import Base as PresentBase
from app.models.quiz import Base as QuizBase

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

DB_URL = (
    f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
)
engine = create_engine(DB_URL, echo=True)


def reset_database():
    PresentBase.metadata.drop_all(bind=engine)
    PresentBase.metadata.create_all(bind=engine)

    QuizBase.metadata.drop_all(bind=engine)
    QuizBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
