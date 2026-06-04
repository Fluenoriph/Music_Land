from app.core.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, SmallInteger
import datetime


class AudioMetadata(Base):
    __tablename__ = 'audio_metadata'

    metadata_id = Column(Integer, primary_key=True, autoincrement=True)
    updated_at = Column(DateTime, insert_default=datetime.datetime.now(), nullable=False)
    artist = Column(Text)
    title = Column(Text)
    album = Column(Text)
    genre = Column(Text)
    year = Column(SmallInteger)
    file_data_id = Column(Integer, ForeignKey('file_data.file_data_id'), nullable=False, unique=True)
