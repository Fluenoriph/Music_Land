import os

from music_land_code.all_files_searcher import AllFilesSearcher
from music_land_code.audio_file_validator_mixin import ValidAudioTypeMixin
from music_land_code.database_level.music_type_struct import MusicTypeStruct
from music_land_code.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor
from music_land_code.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor
from music_land_code.test_code import SEPARATE_LINE


music_dir = r'D:\ELECTRONICA' # Извне


print(SEPARATE_LINE)
print("\nЗапись одного файла в базу - [1]\nПоиск файлов в папке - [2]\n")
program_variant = input("Ввод: ")

if program_variant == "1":
    pass
elif program_variant == "2":
    #target_directory = input("Введите директорию: ")
    all_files = AllFilesSearcher(music_dir) # проверка директории ??

    music_struct = MusicTypeStruct()
    music_struct.add_real_music_files(all_files.files)

    print(SEPARATE_LINE)
    print("Найдено:")

    [print(f"[ {values[music_struct.TYPE_KEYS[0]]} ] - {len(values[music_struct.TYPE_KEYS[2]])}")
     for values in music_struct.data.values()]

    print(SEPARATE_LINE)









    #search_variant = input("\nВведите цифру для поиска определенного формата, для поиска всех введите [0]: ")






















# Check all list !!!
#audio_item = AudioFileAccessor(flac_file)






'''
if audio_item.is_valid_file:




    file_info_extractor = FileGeneralInfoExtractor(flac_file)
    audio_info_extractor = AudioFileFullExtractor(audio_item.audio_info, FLAC_TAG_KEYS)

    print(f"\nИмя файла: {file_info_extractor.file_name}")
    print(f"Размер файла: {file_info_extractor.file_size} MB")

    print(SEPARATE_LINE)
    print(f"Исполнитель: {audio_info_extractor.extracted_tags_data[0]}")
    print(f"Название: {audio_info_extractor.extracted_tags_data[1]}")
    print(f"Альбом: {audio_info_extractor.extracted_tags_data[2]}")
    print(f"Жанр: {audio_info_extractor.extracted_tags_data[3]}")
    print(f"Год: {audio_info_extractor.extracted_tags_data[4]}")

    print(SEPARATE_LINE)
    print(f"Декодер: {audio_info_extractor.extracted_stream_data[0]}")
    print(f"Битрейт: {audio_info_extractor.extracted_stream_data[1]} kbps")
    print(f"Частота дискретизации: {audio_info_extractor.extracted_stream_data[2]} kHz")
    print(f"Время: {audio_info_extractor.extracted_stream_data[3]} min")
    print(f"Разрядность: {audio_info_extractor.extracted_stream_data[4]} bit")
    print(f"Формат звука: {audio_info_extractor.extracted_stream_data[5]}")







else:
    print("\nФайл не определен или поврежден !\n")
'''