# Класс, реализующий операцию CREATE.

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cli_utility.database_level.models.audio_metadata import AudioMetadata
from cli_utility.database_level.models.audio_stream_data import AudioStreamData
from cli_utility.database_level.models.file_data import FileData
from cli_utility.database_level.models.file_type import FileType
from cli_utility.database_level.models.registration_time import RegistrationTime
from cli_utility.music_type_struct import MusicTypeStruct
from cli_utility.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor
from cli_utility.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor


class SessionCreateSet:
    def __init__(self, connection_string, target_data):
        self.engine = create_engine(connection_string, echo=True)
        self.target_data = target_data

    def create_to_database(self):
        with Session(autoflush=False, bind=self.engine) as db_session:
            FileType()

            reg_time_data = RegistrationTime()
            db_session.add(reg_time_data)
            db_session.commit()
            db_session.refresh(reg_time_data)

            for key, value in self.target_data.items():
                if any(value[MusicTypeStruct.DATA_KEYS[2]]):
                    for _ in range(len(value[MusicTypeStruct.DATA_KEYS[2]])):
                        file_info_extractor = FileGeneralInfoExtractor(value[MusicTypeStruct.DATA_KEYS[2]][_][0])

                        audio_info_extractor = AudioFileFullExtractor(value[MusicTypeStruct.DATA_KEYS[2]][_][2],
                                                                      value[MusicTypeStruct.DATA_KEYS[1]])

                        file_data = FileData(file_name=file_info_extractor.file_name,
                                             file_size_mb=file_info_extractor.file_size,
                                             file_location=file_info_extractor.file_location,
                                             file_hash=value[MusicTypeStruct.DATA_KEYS[2]][_][1],
                                             file_type_id=key, reg_time_id=reg_time_data.reg_time_id)

                        db_session.add(file_data)
                        db_session.commit()
                        db_session.refresh(file_data)

                        audio_metadata = AudioMetadata(artist=audio_info_extractor.extracted_tags_data[0],
                                                       title=audio_info_extractor.extracted_tags_data[1],
                                                       album=audio_info_extractor.extracted_tags_data[2],
                                                       genre=audio_info_extractor.extracted_tags_data[3],
                                                       year=audio_info_extractor.extracted_tags_data[4],
                                                       file_data_id=file_data.file_data_id)

                        db_session.add(audio_metadata)
                        db_session.commit()

                        stream_data = AudioStreamData(codec=audio_info_extractor.extracted_stream_data[0],
                                                      bitrate_kbps=audio_info_extractor.extracted_stream_data[1],
                                                      sample_rate_khz=audio_info_extractor.extracted_stream_data[2],
                                                      length_min=audio_info_extractor.extracted_stream_data[3],
                                                      bits_per_sample_bit=audio_info_extractor.extracted_stream_data[4],
                                                      channels=audio_info_extractor.extracted_stream_data[5],
                                                      file_data_id=file_data.file_data_id)

                        db_session.add(stream_data)
                        db_session.commit()
