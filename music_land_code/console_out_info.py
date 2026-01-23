# Класс для вывода информации в консоль.

import os

from music_type_struct import MusicTypeStruct
from music_land_code.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor
from music_land_code.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor
from all_files_searcher import AllFilesSearcher


class ConsoleOutInfo:
    SEPARATE_LINE = '\n-------------------------------------------------------------------------------------------'

    @staticmethod
    def show_about_program():
        print("\n * Music-Land Program *\n Ivan Bogdanov. All rights reserved. 2026")

    @staticmethod
    def show_separate_line():
        print(ConsoleOutInfo.SEPARATE_LINE)

    @staticmethod
    def show_file_extract_data(music_data):
        for values in music_data.values():
            if any(values[MusicTypeStruct.DATA_KEYS[3]]):
                for _ in range(len(values[MusicTypeStruct.DATA_KEYS[3]])):
                    file_info_extractor = FileGeneralInfoExtractor(values[MusicTypeStruct.DATA_KEYS[2]][_])
                    audio_info_extractor = AudioFileFullExtractor(values[MusicTypeStruct.DATA_KEYS[3]][_],
                                                                  values[MusicTypeStruct.DATA_KEYS[1]])

                    ConsoleOutInfo.show_separate_line()

                    print(f"\nИмя файла: {file_info_extractor.file_name}")
                    print(f"Размер файла: {file_info_extractor.file_size} MB")
                    print(f"Расположение: {file_info_extractor.file_location}")
                    print(f"MD5 отпечаток: {values[MusicTypeStruct.DATA_KEYS[4]][_]}")

                    print(f"\nИсполнитель: {audio_info_extractor.extracted_tags_data[0]}")
                    print(f"Название: {audio_info_extractor.extracted_tags_data[1]}")
                    print(f"Альбом: {audio_info_extractor.extracted_tags_data[2]}")
                    print(f"Жанр: {audio_info_extractor.extracted_tags_data[3]}")
                    print(f"Год: {audio_info_extractor.extracted_tags_data[4]}")

                    print(f"\nКодек: {audio_info_extractor.extracted_stream_data[0]}")
                    print(f"Битрейт: {audio_info_extractor.extracted_stream_data[1]} kbps")
                    print(f"Частота дискретизации: {audio_info_extractor.extracted_stream_data[2]} kHz")
                    print(f"Время: {audio_info_extractor.extracted_stream_data[3]} min")
                    print(f"Разрядность: {audio_info_extractor.extracted_stream_data[4]} bit")
                    print(f"Формат звука: {audio_info_extractor.extracted_stream_data[5]}")

    @staticmethod
    def show_finding_info(music_data):
        print("\nНайдено:\n")

        [print(f" [ {values[MusicTypeStruct.DATA_KEYS[0]]} ] - {len(values[MusicTypeStruct.DATA_KEYS[2]])}")
            for values in music_data.values() if len(values[MusicTypeStruct.DATA_KEYS[2]]) != 0]

    @staticmethod
    def enter_data():
        input_data = []

        print(r" Введите путь к папке с файлами или полные пути файлов по очереди. "
              r"Образец: C:\Folder\Subfolder | \file.mp3")
        print(" - после ввода всех файлов введите 's' и нажмите 'Enter'\n")

        while True:             # Счетчик попыток ???
            data = input('> ')

            if data == 's' and any(input_data):
                break
            else:
                if os.path.exists(data):
                    if os.path.isdir(data):
                        return AllFilesSearcher.find_all_files(data)
                    else:
                        input_data.append(data)
                else:
                    print(" Директория не существует ! Повторите...\n")

        return input_data

    @staticmethod
    def try_restart():
        out = r" __/\__/\__ - Для перезапуска введите 'r', для выхода любую клавишу - __/\__/\__"

        return input(f"\n{out}")
