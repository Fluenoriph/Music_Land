from music_land_code.audio_file_accessor import AudioFileAccessor
from music_land_code.data import FLAC_TAG_KEYS
from music_land_code.filedata_extractor.audio_file_full_extractor import AudioFileFullExtractor
from music_land_code.filedata_extractor.file_general_info_extractor import FileGeneralInfoExtractor
from music_land_code.test_code import SEPARATE_LINE


flac_file = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\03 - Rascal & Klone - Winner Takes All.flac"
mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
ape = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
wav_file = r"D:\ELECTRONICA\Miami Mix 2006 mixed by DJ Skorohott\WAV\07 Дорожка 7.wav"
m4a_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"

# Check all list !!!
audio_item = AudioFileAccessor(flac_file)

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