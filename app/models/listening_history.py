import datetime
from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime


class ListeningHistory(Base):
    __tablename__ = "listening_history"

    listen_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    file_data_id = Column(Integer, ForeignKey("file_data.file_data_id"))
    listened_at = Column(DateTime, insert_default=datetime.datetime.now())