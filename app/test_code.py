import mutagen


source = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\13 - D Kay - Monolith.flac"
flac_file = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\03 - Rascal & Klone - Winner Takes All.flac"
mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
ape_file = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
wav_file = r"D:\ELECTRONICA\Miami Mix 2006 mixed by DJ Skorohott\WAV\07 Дорожка 7.wav"
m4a_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"


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

