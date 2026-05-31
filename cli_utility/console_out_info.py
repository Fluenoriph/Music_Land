# Класс для вывода информации в консоль.

from cli_utility.music_type_struct import MusicTypeStruct
from cli_utility.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor
from cli_utility.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor


class ConsoleOutInfo:
    SEPARATE_LINE = '\n-------------------------------------------------------------------------------------------'

    @staticmethod
    def show_file_extract_data(music_data):
        for values in music_data.values():
            if any(values[MusicTypeStruct.DATA_KEYS[2]]):
                for _ in range(len(values[MusicTypeStruct.DATA_KEYS[2]])):
                    file_info_extractor = FileGeneralInfoExtractor(values[MusicTypeStruct.DATA_KEYS[2]][_][0])

                    audio_info_extractor = AudioFileFullExtractor(values[MusicTypeStruct.DATA_KEYS[2]][_][2],
                                                                  values[MusicTypeStruct.DATA_KEYS[1]])

                    print(ConsoleOutInfo.SEPARATE_LINE)

                    print(f"\nИмя файла: {file_info_extractor.file_name}")
                    print(f"Размер файла: {file_info_extractor.file_size} MB")
                    print(f"Расположение: {file_info_extractor.file_location}")
                    print(f"MD5 отпечаток: {values[MusicTypeStruct.DATA_KEYS[2]][_][1]}")

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

        [print(f" [ {values[MusicTypeStruct.DATA_KEYS[0]].upper()} ] - {len(values[MusicTypeStruct.DATA_KEYS[2]])}")
            for values in music_data.values() if len(values[MusicTypeStruct.DATA_KEYS[2]]) != 0]
