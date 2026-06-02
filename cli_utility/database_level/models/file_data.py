from cli_utility.database_level.models.data import Base
from sqlalchemy import Column, Integer, Text, REAL, ForeignKey, BigInteger


class FileData(Base):
    __tablename__ = 'file_data'
    file_data_id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(Text, nullable=False)
    file_size_bytes = Column(BigInteger, nullable=False)
    file_location = Column(Text)
    file_hash = Column(Text, nullable=False)
    file_type_id = Column(Integer, ForeignKey('file_type.file_type_id'), nullable=False)
    batch_id = Column(Integer, ForeignKey('import_batch.batch_id'), nullable=False)
