# Базовый класс поиска файлов по расширению.

import os
from abc import ABC, abstractmethod


class BaseFileTypeSearcher(ABC):

    def __init__(self, target_directory, target_file_type):
        self.all_files = BaseFileTypeSearcher.find_all_files(target_directory)
        self.target_file_type = target_file_type
        self.create_file_extension = lambda file_type: '.' + file_type

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

    @abstractmethod
    def separating_files_at_type(self):
        pass

    def get_files_at_type(self, file_type):
        files = []

        [files.append(file) for file in self.all_files if file.upper().endswith(self.create_file_extension(file_type))]

        return files
