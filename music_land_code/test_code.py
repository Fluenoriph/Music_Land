import mutagen


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

