from music_land_code.database_level.data import Base
from sqlalchemy import Column, Integer, Text, ForeignKey


class AudioMetadata(Base):
    __tablename__ = 'audio_metadata'
    metadata_id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(Text)
    title = Column(Text)
    album = Column(Text)
    genre = Column(Text)
    year = Column(Text)
    file_data_id = Column(Integer, ForeignKey('file_data.file_data_id'), nullable=False)
