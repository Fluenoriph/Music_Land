from music_land_code.database_level.models.data import Base
from sqlalchemy import Column, Integer, Text, REAL, ForeignKey


class FileData(Base):
    __tablename__ = 'file_data'
    file_data_id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(Text, nullable=False)
    file_size_mb = Column(REAL, nullable=False)
    file_location = Column(Text)
    file_type_id = Column(Integer, ForeignKey('file_type.file_type_id'), nullable=False) # настроить каскад
    reg_time_id = Column(Integer, ForeignKey('registration_time.reg_time_id'), nullable=False)
