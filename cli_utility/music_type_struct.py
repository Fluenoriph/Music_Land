# Класс для создания структуры валидированных аудио файлов.

import threading
import queue
import re
from cli_utility.audio_file_validator import AudioFileValidator as AudioChecker
from cli_utility.sha256_digest import SHA256Digest

# May be split this class ??????? -----------------------------
# Может в дальнейшем нужно будет искать другие форматы !!
class MusicTypeStruct(AudioChecker):
    DATA_KEYS = ('format', 'metadata_tags', 'audio_file_composite_data')

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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def extract_audio_file_type(stream_info):
        match = re.search(re.compile(r'audio/.+', re.IGNORECASE), stream_info)

        if match:
            return match.group().split('/')[-1].strip(')')
        else:
            return None

    def add_real_one_music_file(self, file):
        audio_type = AudioChecker.check_file(file)

        if audio_type is not False:
            for key in self.data.keys():    # test !!!
                if (MusicTypeStruct.extract_audio_file_type(audio_type.pprint()) ==
                            self.data[key][MusicTypeStruct.DATA_KEYS[0]]):
                    self.data[key][MusicTypeStruct.DATA_KEYS[2]].append((file, SHA256Digest.compute_digest(file),
                                                                         audio_type))
                    break

    def add_real_some_music_files(self, random_files):
        q = queue.Queue()

        for random_file in random_files:
            q.put(random_file)

        def audio_type_task_operation():
            while not q.empty():
                file = q.get()
                self.add_real_one_music_file(file)
                q.task_done()

        MAX_THREADS = 100
        threads = []
        for _ in range(min(MAX_THREADS, q.qsize())):
            thread = threading.Thread(target=audio_type_task_operation)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
