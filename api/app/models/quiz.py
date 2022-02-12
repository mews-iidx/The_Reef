from app.db import Base
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import current_timestamp


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(Integer, index=True, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        nullable=False,
    )
