# Класс, который проверяет, действительно ли это аудиофайл.

import mutagen


class AudioFileValidator:
    
    @staticmethod
    def check_file(file_fullpath):
        try:
            audio_file_type = mutagen.File(file_fullpath)
        except mutagen.MutagenError:
            return False
        else:
            return audio_file_type
