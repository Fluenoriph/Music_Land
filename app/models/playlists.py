import datetime
from app.core.database import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey


class Playlists(Base):
    __tablename__ = "playlists"

    playlist_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(Text, nullable=False)
    created_at = Column(DateTime, insert_default=datetime.datetime.now())