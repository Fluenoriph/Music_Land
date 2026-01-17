# Поиск файлов многих типов.

from base_filetype_searcher import BaseFileTypeSearcher


class MoreFileTypeSearcher(BaseFileTypeSearcher):
    def __init__(self, target_directory, target_file_type):
        super().__init__(target_directory, target_file_type)
        self.separated_files = {}

    def separating_files_at_type(self):
        for file_type in self._target_file_type:
            current_files = self.get_files_at_type(file_type)

            if len(current_files) != 0:
                self.separated_files[file_type] = current_files