import os
import abc


music_dir = 'D:\\ELECTRONICA'
music_file_types = ['APE', 'FLAC', 'M4A', 'MP3', 'MPC', 'WAV']


class BaseFileTypeSearcher(abc.ABC):

    def __init__(self, target_directory, target_file_type):
        self._all_files = BaseFileTypeSearcher.find_all_files(target_directory)
        self._target_file_type = target_file_type
        self._create_file_extension = lambda file_type: '.' + file_type
        self.__separated_files = None

    @property
    def separated_files(self):
        return self.__separated_files

    @separated_files.setter
    def separated_files(self, separated_files):
        self.__separated_files = separated_files

    @staticmethod
    def find_all_files(path):
        files = []

        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.path)
                elif entry.is_dir():
                    files.extend(BaseFileTypeSearcher.find_all_files(entry.path))

        return files

    @abc.abstractmethod
    def separating_files_to_type(self):
        pass

    def get_files_at_type(self, file_type):
        files = []

        [files.append(file) for file in self._all_files if file.upper().endswith(self._create_file_extension(file_type))]

        return files


class OneFileTypeSearcher(BaseFileTypeSearcher):

    def __init__(self, target_directory, target_file_type):
        super().__init__(target_directory, target_file_type)

    def separating_files_to_type(self):
        self.separated_files = self.get_files_at_type(self._target_file_type)


class MoreFileTypeSearcher(BaseFileTypeSearcher):
    def __init__(self, target_directory, target_file_type):
        super().__init__(target_directory, target_file_type)

    def separating_files_to_type(self):
        self.separated_files = {}

        for file_type in self._target_file_type:
            current_files = self.get_files_at_type(file_type)

            if len(current_files) != 0:
                self.separated_files[file_type] = current_files


# High level classes >>>>
'''
search_one_type = OneFileTypeSearcher(music_dir, music_file_types[3])
search_one_type.separating_files_to_type()

[print(file) for file in search_one_type.separated_files]
print(len(search_one_type.separated_files))
'''

more_type_searcher = MoreFileTypeSearcher(music_dir, music_file_types)
more_type_searcher.separating_files_to_type()

for f_type in music_file_types:
    file_type_sum = len(more_type_searcher.separated_files[f_type])

    print(f"{f_type} - [ {file_type_sum} ]")










