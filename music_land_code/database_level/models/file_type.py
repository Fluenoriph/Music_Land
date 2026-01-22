from music_land_code.database_level.models.data import Base
from sqlalchemy import Column, Integer, Text


class FileType(Base):
    __tablename__ = 'file_type'
    file_type_id = Column(Integer, primary_key=True, autoincrement=True)
    file_type_name = Column(Text, nullable=False, unique=True)
