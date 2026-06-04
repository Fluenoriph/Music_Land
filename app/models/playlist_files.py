from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey


class PlaylistFiles(Base):
    __tablename__ = 'playlist_files'

    playlist_id = Column(Integer, ForeignKey('playlists.playlist_id'), primary_key=True)
    file_data_id = Column(Integer, ForeignKey('file_data.file_data_id'), primary_key=True)