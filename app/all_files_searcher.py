# Класс для создания списка всех файлов (всех типов) в директории.

import os


class AllFilesSearcher:
            
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
