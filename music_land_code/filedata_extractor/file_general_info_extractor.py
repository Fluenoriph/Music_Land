# Класс для извлечения основной информации о файле.

import os
from music_land_code.filedata_extractor.round_result import RoundResult


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