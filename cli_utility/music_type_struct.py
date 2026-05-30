# Структура для поиска музыкальных файлов.

import threading
import queue
import re
from audio_file_validator import AudioFileValidator as AudioChecker
from file_digest import FileDigest


class MusicTypeStruct(AudioChecker):
    DATA_KEYS = ('format', 'metadata_tags', 'audio_file_composite_data')
    # Проследить во всем коде эти ключи
    def __init__(self):
        self.__data = {

            1: {
                MusicTypeStruct.DATA_KEYS[0]: 'ape',
                MusicTypeStruct.DATA_KEYS[1]: ('ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'YEAR'),
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            2: {
                MusicTypeStruct.DATA_KEYS[0]: 'flac',
                MusicTypeStruct.DATA_KEYS[1]: ('ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'DATE'),
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            3: {
                MusicTypeStruct.DATA_KEYS[0]: 'mp4',
                MusicTypeStruct.DATA_KEYS[1]: ('\xa9ART', '\xa9nam', '\xa9alb', '\xa9gen', '\xa9day'),
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            4: {
                MusicTypeStruct.DATA_KEYS[0]: 'mp3',
                MusicTypeStruct.DATA_KEYS[1]: ('TPE1', 'TIT2', 'TALB', 'TCON', 'TDRC'),
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            5: {
                MusicTypeStruct.DATA_KEYS[0]: 'x-musepack',
                MusicTypeStruct.DATA_KEYS[1]: ('ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'YEAR'),
                MusicTypeStruct.DATA_KEYS[2]: []
            },

            6: {
                MusicTypeStruct.DATA_KEYS[0]: 'wav',
                MusicTypeStruct.DATA_KEYS[1]: None,
                MusicTypeStruct.DATA_KEYS[2]: []
            }
        }
                # may be split this class ??????? -----------------------------
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def add_real_music_file(self, source_files):
        if len(source_files) > 1:
            q = queue.Queue()

            for random_file in source_files:
                q.put(random_file)

            def audio_type_task_operation():
                while not q.empty():
                    file = q.get()
                    self.add_valid_audio_to_data(file)
                    q.task_done()

            MAX_THREADS = 100
            threads = []
            for _ in range(min(MAX_THREADS, q.qsize())):
                t = threading.Thread(target=audio_type_task_operation)
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        else:
            self.add_valid_audio_to_data(source_files[0])

    @staticmethod
    def extract_audio_file_type(stream_info):
        match = re.search(re.compile(r'audio/.+', re.IGNORECASE), stream_info)

        if match:
            return match.group().split('/')[-1].strip(')')
        else:
            return None

    def add_valid_audio_to_data(self, file):
        audio_type = AudioChecker.check_file(file)

        if audio_type is not False:
            for key in self.data.keys():
                if (MusicTypeStruct.extract_audio_file_type(audio_type.pprint()) ==
                            self.data[key][MusicTypeStruct.DATA_KEYS[0]]):
                    self.data[key][MusicTypeStruct.DATA_KEYS[2]].append((file, FileDigest.md5_digest(file), audio_type))
                    break
