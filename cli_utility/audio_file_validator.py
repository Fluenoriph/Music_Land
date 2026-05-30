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
            if type(audio_file_type) is not type(None):
                return audio_file_type
            else:
                return False
