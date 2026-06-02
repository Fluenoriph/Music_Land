# Класс для извлечения аудио данных с информацией потока.

from cli_utility.filedata_extractor.audio_file_metadata_extractor import AudioFileMetadataExtractor
from cli_utility.filedata_extractor.unit_converter import UnitConverter


class AudioFileFullExtractor(AudioFileMetadataExtractor):
    def __init__(self, audio_type, tag_keys=None):
        super().__init__(audio_type, tag_keys)
        self.__extracted_stream_data = []

        self.extracted_stream_data.append(self.audio_type.pprint().split('\n')[0].split(',')[0])
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
    # APE не содержит битрейт, а MP3 и MPC не содержат разрядность.

    def extract_exist_bitrate(self):
        try:
            self.audio_type.info.bitrate
        except AttributeError:
            return None
        else:
            return UnitConverter.round_result(self.audio_type.info.bitrate / UnitConverter.KILO_CONVERT_INDEX,
                                              UnitConverter.INT_ROUND_INDEX)

    def extract_exist_sample_rate(self):
        try:
            self.audio_type.info.sample_rate
        except AttributeError:
            return None
        else:
            return UnitConverter.round_result(self.audio_type.info.sample_rate / UnitConverter.KILO_CONVERT_INDEX,
                                              UnitConverter.INT_ROUND_INDEX)

    def extract_exist_length(self):
        try:
            self.audio_type.info.length
        except AttributeError:
            return None
        else:
            return self.audio_type.info.length

                #UnitConverter.round_result(self.audio_type.info.length / AudioFileFullExtractor.MINUTES_CONVERT_INDEX,
                                              #UnitConverter.FLOAT_ROUND_INDEX))

    def extract_exist_bits_per_sample(self):
        try:
            self.audio_type.info.bits_per_sample
        except AttributeError:
            return None
        else:
            return self.audio_type.info.bits_per_sample

    def extract_exist_channels(self):
        try:
            self.audio_type.info.channels
        except AttributeError:
            return None
        else:
            if self.audio_type.info.channels == 2:
                return "Stereo"
            elif self.audio_type.info.channels == 1:
                return "Mono"
            else:
                return "Multi_channel"
