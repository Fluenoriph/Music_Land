# Класс для извлечения основной информации о файле.

import os
from cli_utility.filedata_extractor.unit_converter import UnitConverter


class FileGeneralInfoExtractor:
    def __init__(self, file):
        self.__file_location = os.path.dirname(file)
        self.__file_name = os.path.basename(file)
        self.__file_size = os.path.getsize(file) #/ FileGeneralInfoExtractor.MEGABYTE_CONVERT_INDEX

    @property
    def file_location(self):
        return self.__file_location

    @property
    def file_name(self):
        return self.__file_name

    @property
    def file_size(self):
        return self.__file_size

            #UnitConverter.round_result(self.__file_size, UnitConverter.FLOAT_ROUND_INDEX))
