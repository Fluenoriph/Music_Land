from cli_utility.database_level.models.data import Base
from sqlalchemy import Column, Integer, DateTime, Text
import datetime


class ImportBatch(Base):
    __tablename__ = 'import_batch'
    batch_id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, insert_default=datetime.datetime.now(), nullable=False)
    description = Column(Text, nullable=True)