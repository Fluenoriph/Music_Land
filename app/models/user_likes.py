from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey


class UserLikes(Base):
    __tablename__ = 'user_likes'

    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    file_data_id = Column(Integer, ForeignKey('file_data.file_data_id'), primary_key=True)