# Поиск файлов одного единственного типа.

from music_land_code.filetype_searcher.base_filetype_searcher import BaseFileTypeSearcher


class OneFileTypeSearcher(BaseFileTypeSearcher):

    def __init__(self, target_directory, target_file_type):
        super().__init__(target_directory, target_file_type)

    def separating_files_at_type(self):
        self.separated_files = self.get_files_at_type(self.target_file_type)