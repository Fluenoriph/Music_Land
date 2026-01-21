# Структура для поиска музыкальных файлов.

from music_land_code.audio_file_validator_mixin import ValidAudioTypeMixin as AudioChecker


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

    TYPE_KEYS = ('format', 'metadata_tags', 'files', 'audio')

    def __init__(self):
        self.__data = {

            1: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.MONKEYS_AUDIO_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            },

            2: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.FLAC_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: MusicTypeStruct.FLAC_TAG_KEYS,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            },

            3: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.M4A_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: MusicTypeStruct.M4A_TAG_KEYS,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            },

            4: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.MP3_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: MusicTypeStruct.MP3_ID3TYPE_TAG_KEYS,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            },

            5: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.MUSEPACK_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            },

            6: {
                MusicTypeStruct.TYPE_KEYS[0]: MusicTypeStruct.WAVE_TYPE,
                MusicTypeStruct.TYPE_KEYS[1]: None,
                MusicTypeStruct.TYPE_KEYS[2]: [],
                MusicTypeStruct.TYPE_KEYS[3]: []
            }
        }

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def add_real_music_files(self, source_files):
        for file in source_files:
            audio_type = AudioChecker.check_file(file)

            if audio_type is not False:          # можно проверить формат также по данным потока
                for key, value in self.data.items():
                    if file.upper().endswith('.' + self.data[key][MusicTypeStruct.TYPE_KEYS[0]]):
                        self.data[key][MusicTypeStruct.TYPE_KEYS[2]].append(file)
                        self.data[key][MusicTypeStruct.TYPE_KEYS[3]].append(audio_type)
