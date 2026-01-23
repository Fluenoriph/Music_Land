# Класс для создания списка всех файлов (всех типов) в директории.

import os


class AllFilesSearcher:
    def __init__(self, path):
        self.__files = AllFilesSearcher.find_all_files(path)

    @property
    def files(self):
        return self.__files

    @staticmethod
    def find_all_files(path):
        files = []

        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.path)
                elif entry.is_dir():
                    files.extend(AllFilesSearcher.find_all_files(entry.path))

        return files
