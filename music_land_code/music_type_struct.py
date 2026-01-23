# Структура для поиска музыкальных файлов.
import hashlib

from audio_file_validator import ValidAudioType as AudioChecker
from music_land_code.filedata_extractor.file_digest import FileDigest


class MusicTypeStruct(AudioChecker, FileDigest):
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

    DATA_KEYS = ('format', 'metadata_tags', 'files', 'audio', 'file_hashsum')

    def __init__(self):
        self.__data = {

            1: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MONKEYS_AUDIO_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
            },

            2: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.FLAC_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.FLAC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
            },

            3: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.M4A_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.M4A_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
            },

            4: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MP3_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.MP3_ID3TYPE_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
            },

            5: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.MUSEPACK_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: MusicTypeStruct.APE_MPC_TAG_KEYS,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
            },

            6: {
                MusicTypeStruct.DATA_KEYS[0]: MusicTypeStruct.WAVE_TYPE,
                MusicTypeStruct.DATA_KEYS[1]: None,
                MusicTypeStruct.DATA_KEYS[2]: [],
                MusicTypeStruct.DATA_KEYS[3]: [],
                MusicTypeStruct.DATA_KEYS[4]: []
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
                for key, value in self.data.items():
                    if file.upper().endswith('.' + self.data[key][MusicTypeStruct.DATA_KEYS[0]]):
                        self.data[key][MusicTypeStruct.DATA_KEYS[2]].append(file)
                        self.data[key][MusicTypeStruct.DATA_KEYS[3]].append(audio_type)

    def compute_file_hashsum(self):
        for values in self.data.values():
            if any(values[MusicTypeStruct.DATA_KEYS[2]]):
                for file in values[MusicTypeStruct.DATA_KEYS[2]]:
                    hash_sum = FileDigest.md5(file)

                    if hash_sum not in values[MusicTypeStruct.DATA_KEYS[4]]:   # delete to index ??
                        values[MusicTypeStruct.DATA_KEYS[4]].append(hash_sum)
