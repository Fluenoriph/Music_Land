# Класс для валидации аудиофайла.

import mutagen


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