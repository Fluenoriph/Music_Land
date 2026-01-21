# Класс для валидации аудиофайла.

import mutagen


class ValidAudioTypeMixin:
    @staticmethod
    def check_file(file_fullpath):
        try:
            audio = mutagen.File(file_fullpath)
        except mutagen.MutagenError:
            return False
        else:
            return audio
