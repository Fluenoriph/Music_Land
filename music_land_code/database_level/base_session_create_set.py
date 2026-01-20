from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from music_land_code.database_level.models.registration_time import RegistrationTime


class BaseSessionCreateSet(ABC):
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string, echo=True)

    @abstractmethod
    def create_set(self, file):
        pass

    @staticmethod
    def create_reg_time_data_and_get_id(db_session):
        reg_time_data = RegistrationTime()

        db_session.add(reg_time_data)
        db_session.commit()
        db_session.refresh(reg_time_data)

        return reg_time_data.reg_time_id







    def create_one_file_data_set(self):
