from app.db import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import current_timestamp


class Present(Base):
    __tablename__ = "presents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    present_category_id = Column(
        Integer, ForeignKey("present_categories.id"), index=True, nullable=False
    )
    amazon_url = Column(String(255), nullable=True)
    image_path = Column(String(255), nullable=True)
    winner = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        nullable=False,
    )


class PresentCategory(Base):
    __tablename__ = "present_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        nullable=False,
    )

    presents = relationship("Present", backref="present_categories")
