from app.core.database import Base
from sqlalchemy import Column, Integer, Text, VARCHAR, DateTime
import datetime


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, insert_default=datetime.datetime.now(), nullable=False)
