import mutagen
from one_filetype_searcher import OneFileTypeSearcher
from audio_file_metadata_extractor import FileGeneralInfoExtractor, AudioFileAccessor, AudioFileFullExtractor


music_dir = r'D:\ELECTRONICA'

MONKEYS_AUDIO_TYPE = 'APE'
FLAC_TYPE = 'FLAC'
M4A_TYPE = 'M4A'
MP3_TYPE = 'MP3'
MUSEPACK_TYPE = 'MPC'
WAVE_TYPE = 'WAV'

MP3_ID3TYPE_TAG_KEYS = ['TPE1', 'TIT2', 'TALB', 'TCON', 'TDRC']
APE_MPC_TAG_KEYS = ['ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'YEAR']
FLAC_TAG_KEYS = ['ARTIST', 'TITLE', 'ALBUM', 'GENRE', 'DATE']
M4A_TAG_KEYS = ['\xa9ART', '\xa9nam', '\xa9alb', '\xa9gen', '\xa9day']

SEPARATE_LINE = '-------------------------------------------------------------------------------------------'

# Вывести данные словаря в консоль

def show_dictionary_data(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

# Проверка на существование параметра потока в метаданных файла.

def check_the_stream_parameter(parameter):
    try:
        parameter
    except AttributeError:
        return None
    else:
        return parameter

# Извлечение метаданных из списка файлов одного типа.

def extract_audio_data_at_filetype_list(files, tags=None):
    file_count = 0

    bad_files = {}

    for file in files:
        file_count += 1

        try:
            audio_info = mutagen.File(file)
        except mutagen.MutagenError as bad_file_exception:
            print(bad_file_exception)

            bad_files[file_count] = file
            continue
        else:
            stream_info = audio_info.pprint().split('\n')[0]
            stream_type = stream_info.split(',')[0]

            tags_data = []

            if (tags is not None) and (audio_info.tags is not None):
                for tag in tags:
                    if tag in audio_info.tags:
                        tags_data.append(audio_info[tag])
                    else:
                        tags_data.append(None)

            print(f"Файл № {file_count}: {file}")
            [print(tag_value) for tag_value in tags_data]

            print(f"\nДекодер: {stream_type}")

            ch = audio_info.info.channels
            if ch == 1 or 2:
                print(ch)
            else:
                print(ch)
                break

            #print(f"Битрейт: {check_the_stream_parameter(audio_info.info.bitrate)}")
            #print(f"Частота дискретизации: {check_the_stream_parameter(audio_info.info.sample_rate)}")
            #print(f"Время: {check_the_stream_parameter(audio_info.info.length)}")
            #print(f"Разрядность: {check_the_stream_parameter(audio_info.info.bits_per_sample)}")

    print(f"Обработано - {file_count} файлов\n")
    print("Поврежденные файлы:\n")

    show_dictionary_data(bad_files)

'''
search_one_type = OneFileTypeSearcher(music_dir, WAVE_TYPE)
search_one_type.separating_files_at_type()
[print(file) for file in search_one_type.separated_files]
print(len(search_one_type.separated_files))
extract_audio_data_at_filetype_list(search_one_type.separated_files)
'''

flac_file = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\03 - Rascal & Klone - Winner Takes All.flac"
mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
ape = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
wav_file = r"D:\ELECTRONICA\Miami Mix 2006 mixed by DJ Skorohott\WAV\07 Дорожка 7.wav"
m4a_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"


audio_validator = AudioFileAccessor(flac_file)

if audio_validator.is_valid_file:
    file_info_extractor = FileGeneralInfoExtractor(flac_file)
    audio_info_extractor = AudioFileFullExtractor(audio_validator.audio_info, FLAC_TAG_KEYS)

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





