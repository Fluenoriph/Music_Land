from app.core.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, BigInteger, VARCHAR, DateTime
import datetime


class FileData(Base):
    __tablename__ = 'file_data'

    file_data_id = Column(Integer, primary_key=True, autoincrement=True)
    file_location = Column(Text)
    file_name = Column(Text, nullable=False)
    file_size_bytes = Column(BigInteger, nullable=False)
    file_hash = Column(VARCHAR(64), nullable=False, unique=True)
    created_at = Column(DateTime, insert_default=datetime.datetime.now(), nullable=False)

    file_type_id = Column(Integer, ForeignKey('file_type.file_type_id'), nullable=False)
    batch_id = Column(Integer, ForeignKey('import_batch.batch_id'), nullable=True) # ??? null
