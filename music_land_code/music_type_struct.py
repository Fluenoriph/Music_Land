# Структура для поиска музыкальных файлов.

from audio_file_validator import ValidAudioType as AudioChecker
from audio_file import AudioFile


class MusicTypeStruct(AudioChecker):
    MONKEYS_AUDIO_TYPE = 'APE'
    FLAC_TYPE = 'FLAC'
    M4A_TYPE = 'M4A'
    MP3_TYPE = 'MP3'
    MUSEPACK_TYPE = 'MPC'
    WAVE_TYPE = 'WAV'

    APE_MPC_TAG_KEYS = ('ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'YEAR')
    FLAC_TAG_KEYS = ('ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'DATE')
    M4A_TAG_KEYS = ('\xa9ART', '\xa9nam', '\xa9alb', '\xa9gen', '\xa9day')
    MP3_ID3TYPE_TAG_KEYS = ('TPE1', 'TIT2', 'TALB', 'TCON', 'TDRC')

    DATA_KEYS = ('format', 'metadata_tags', 'audio_type')

    def __init__(self):
        self.__data = {

            1: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MONKEYS_AUDIO_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            2: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.FLAC_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.FLAC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            3: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.M4A_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.M4A_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            4: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MP3_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.MP3_ID3TYPE_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            5: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MUSEPACK_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            6: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.WAVE_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: None,
                MusicTypeStruct.DATA_KEYS[2]: []
            }
        }

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def add_real_music_file(self, source_files):
        for file in source_files:
            audio_type = AudioChecker.check_file(file)

            if audio_type is not False:                          # можно проверить формат также по данным потока
                for key in self.data.keys():
                    if file.upper().endswith('.' + self.data[key][MusicTypeStruct.DATA_KEYS[0]]):
                        self.data[key][MusicTypeStruct.DATA_KEYS[2]].append(AudioFile(file=file, audio_type=audio_type))
