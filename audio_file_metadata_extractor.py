import os
import mutagen
from decimal import Decimal, ROUND_HALF_UP


class RoundResult:
    FLOAT_ROUND_INDEX = ".01"
    INT_ROUND_INDEX = "1"

    @staticmethod
    def round_result(result, round_index):
        return Decimal(result).quantize(Decimal(round_index), rounding=ROUND_HALF_UP)


class FileGeneralInfoExtractor:
    MB_CONVERT_INDEX = 1048576

    def __init__(self, file_path):
        self.__file_name = os.path.basename(file_path)
        self.__file_size = os.path.getsize(file_path) / FileGeneralInfoExtractor.MB_CONVERT_INDEX

    @property
    def file_name(self):
        return self.__file_name

    @property
    def file_size(self):
        return RoundResult.round_result(self.__file_size, RoundResult.FLOAT_ROUND_INDEX)


class AudioFileAccessor:
    def __init__(self, file_path):
        self.__is_valid_file = None

        try:
            self.__audio_info = mutagen.File(file_path)
        except mutagen.MutagenError:
            self.__is_valid_file = False
        else:
            self.__is_valid_file = True

    @property
    def is_valid_file(self):
        return self.__is_valid_file

    @property
    def audio_info(self):
        return self.__audio_info


class AudioFileMetadataExtractor:
    def __init__(self, audio_info, tag_keys=None):
        self.audio_info = audio_info
        self.tag_keys = tag_keys
        self.__extracted_tags_data = []

        is_tags_exist = (self.tag_keys is not None) and (self.audio_info.tags is not None)

        if is_tags_exist:
            for tag in self.tag_keys:
                if tag in self.audio_info.tags:
                    tag_value = str(self.audio_info[tag])

                    self.extracted_tags_data.append(tag_value.strip("[']"))
                else:
                    self.extracted_tags_data.append(None)

    @property
    def extracted_tags_data(self):
        return self.__extracted_tags_data

    @extracted_tags_data.setter
    def extracted_tags_data(self, value):
        self.__extracted_tags_data = value


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
