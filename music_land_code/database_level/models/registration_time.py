from music_land_code.database_level.data import Base
from sqlalchemy import Column, Integer, DateTime
import datetime


class RegistrationTime(Base):
    __tablename__ = 'registration_time'
    reg_time_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_time_value = Column(DateTime, insert_default=datetime.datetime.now())
