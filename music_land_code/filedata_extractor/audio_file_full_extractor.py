# Класс для извлечения аудиоданных с информацией потока.

from music_land_code.filedata_extractor.audio_file_metadata_extractor import AudioFileMetadataExtractor
from music_land_code.filedata_extractor.round_result import RoundResult


class AudioFileFullExtractor(AudioFileMetadataExtractor):
    KILO_CONVERT_INDEX = 1000
    MINUTES_CONVERT_INDEX = 60

    def __init__(self, audio_info, tag_keys=None):
        super().__init__(audio_info, tag_keys)
        self.__extracted_stream_data = []

        self.extracted_stream_data.append(self.audio_info.pprint().split('\n')[0].split(',')[0])
        self.extracted_stream_data.append(self.extract_exist_bitrate())
        self.extracted_stream_data.append(self.extract_exist_sample_rate())
        self.extracted_stream_data.append(self.extract_exist_length())
        self.extracted_stream_data.append(self.extract_exist_bits_per_sample())
        self.extracted_stream_data.append(self.extract_exist_channels())

    @property
    def extracted_stream_data(self):
        return self.__extracted_stream_data

    @extracted_stream_data.setter
    def extracted_stream_data(self, value):
        self.__extracted_stream_data = value

    # Методы для извлечения данных потока. Проверяются все.
    # APE не содержит битрейт, а MP3 & MPC не содержат разрядность.

    def extract_exist_bitrate(self):
        try:
            self.audio_info.info.bitrate
        except AttributeError:
            return None
        else:
            return RoundResult.round_result(self.audio_info.info.bitrate / AudioFileFullExtractor.KILO_CONVERT_INDEX,
                                            RoundResult.INT_ROUND_INDEX)

    def extract_exist_sample_rate(self):
        try:
            self.audio_info.info.sample_rate
        except AttributeError:
            return None
        else:
            return RoundResult.round_result(self.audio_info.info.sample_rate / AudioFileFullExtractor.KILO_CONVERT_INDEX,
                                            RoundResult.INT_ROUND_INDEX)

    # Прверить деление чисел с запятой !!!!

    def extract_exist_length(self):
        try:
            self.audio_info.info.length
        except AttributeError:
            return None
        else:
            return RoundResult.round_result(self.audio_info.info.length / AudioFileFullExtractor.MINUTES_CONVERT_INDEX,
                                            RoundResult.FLOAT_ROUND_INDEX)

    def extract_exist_bits_per_sample(self):
        try:
            self.audio_info.info.bits_per_sample
        except AttributeError:
            return None
        else:
            return self.audio_info.info.bits_per_sample

    def extract_exist_channels(self):
        try:
            self.audio_info.info.channels
        except AttributeError:
            return None
        else:
            if self.audio_info.info.channels == 2:
                return "Stereo"
            elif self.audio_info.info.channels == 1:
                return "Mono"
            else:
                return "Multi_channel"
