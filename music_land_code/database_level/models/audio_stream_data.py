from music_land_code.database_level.data import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, REAL


class AudioStreamData(Base):
    __tablename__ = 'audio_stream_data'
    stream_data_id = Column(Integer, primary_key=True, autoincrement=True)
    decoder = Column(Text, nullable=False)
    bitrate_kbps = Column(Integer)
    sample_rate_khz = Column(Integer)
    length_min = Column(REAL)
    bits_per_sample_bit = Column(Integer)
    channels = Column(Text)
    file_data_id = Column(Integer, ForeignKey('file_data.file_data_id'), nullable=False)
