import os
from music_land_code.all_files_searcher import AllFilesSearcher
from music_land_code.database_level.music_type_struct import MusicTypeStruct
from music_land_code.database_level.session_create_set import SessionCreateSet
from music_land_code.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor
from music_land_code.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor
from music_land_code.test_code import SEPARATE_LINE


music_dir = r'D:\ELECTRONICA' # Извне is not dir, a file ????
connect = "postgresql://postgres:robov@localhost:5432/music_land"


print(SEPARATE_LINE)
#source = input("\nВведите директорию для поиска или путь к файлу для записи в базу > Образец: C:\Folder\Subfolder | file.mp3\n ")
print(SEPARATE_LINE)

source = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\13 - D Kay - Monolith.flac"
flac_file = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\03 - Rascal & Klone - Winner Takes All.flac"
mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
ape_file = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
wav_file = r"D:\ELECTRONICA\Miami Mix 2006 mixed by DJ Skorohott\WAV\07 Дорожка 7.wav"
m4a_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"

if os.path.exists(source):
    music_struct = MusicTypeStruct()

    if os.path.isdir(source):
        print("Source is folder !")
        # database set !!
    else:
        print("Source is file !")

        #files = [source] add ??

        music_struct.add_real_music_file([source, flac_file, mp3_file, ape_file, mpc_file, wav_file, m4a_file])

        database_set = SessionCreateSet(connect, music_struct.data)
        database_set.create_to_database()

        print(SEPARATE_LINE)
        print("OK ! Data is add to database !")
else:
    print("Source does not exist !")









'''
if source == "1":
    pass
elif source == "2":
    #target_directory = input("Введите директорию: ")
    all_files = AllFilesSearcher(music_dir) # проверка директории ??

    music_struct = MusicTypeStruct()
    music_struct.add_real_music_file(all_files.files)

    print(SEPARATE_LINE)
    print("Найдено:")

    [print(f" [ {values[music_struct.TYPE_KEYS[0]]} ] - {len(values[music_struct.TYPE_KEYS[2]])}"
           f" | Audio Type: {len(values[music_struct.TYPE_KEYS[3]])} ")
     for values in music_struct.data.values()]

    print(SEPARATE_LINE)


    for values in music_struct.data.values():
        for _ in range(6): # len ???
            file_info_extractor = FileGeneralInfoExtractor(values[music_struct.TYPE_KEYS[2]][_])
            audio_info_extractor = AudioFileFullExtractor(values[music_struct.TYPE_KEYS[3]][_], values[music_struct.TYPE_KEYS[1]])

            print(f"\n\nИмя файла: {file_info_extractor.file_name}")
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
            
            -------------------------**************************
            
            for values in music_struct.data.values():
            if any(values[music_struct.TYPE_KEYS[3]]):
                for _ in range(len(values[music_struct.TYPE_KEYS[3]])):
                    file_info_extractor = FileGeneralInfoExtractor(values[music_struct.TYPE_KEYS[2]][_])
                    audio_info_extractor = AudioFileFullExtractor(values[music_struct.TYPE_KEYS[3]][_],
                                                                  values[music_struct.TYPE_KEYS[1]])

                    print(SEPARATE_LINE)
                    print(f"\nИмя файла: {file_info_extractor.file_name}")
                    print(f"Размер файла: {file_info_extractor.file_size} MB")
                    print(f"Расположение: {file_info_extractor.file_location}")

                    print(f"\nИсполнитель: {audio_info_extractor.extracted_tags_data[0]}")
                    print(f"Название: {audio_info_extractor.extracted_tags_data[1]}")
                    print(f"Альбом: {audio_info_extractor.extracted_tags_data[2]}")
                    print(f"Жанр: {audio_info_extractor.extracted_tags_data[3]}")
                    print(f"Год: {audio_info_extractor.extracted_tags_data[4]}")

                    print(f"\nДекодер: {audio_info_extractor.extracted_stream_data[0]}")
                    print(f"Битрейт: {audio_info_extractor.extracted_stream_data[1]} kbps")
                    print(f"Частота дискретизации: {audio_info_extractor.extracted_stream_data[2]} kHz")
                    print(f"Время: {audio_info_extractor.extracted_stream_data[3]} min")
                    print(f"Разрядность: {audio_info_extractor.extracted_stream_data[4]} bit")
                    print(f"Формат звука: {audio_info_extractor.extracted_stream_data[5]}\n")
            
'''