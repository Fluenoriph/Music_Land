import os.path

from console_out_info import ConsoleOutInfo
from music_type_struct import MusicTypeStruct
from music_land_code.database_level.session_create_set import SessionCreateSet


connect = "postgresql://postgres:robov@localhost:5432/music_land"

out_info = ConsoleOutInfo()
out_info.show_about_program()

while True:
    out_info.show_separate_line()

    input_data = out_info.enter_data()

    music_struct = MusicTypeStruct()
    music_struct.add_real_music_file(input_data)

    out_info.show_finding_info(music_struct.data)

    is_one_file = (os.path.isfile(input_data[0])) and (len(input_data) == 1)

    if is_one_file:
        out_info.show_file_extract_data(music_struct.data)
        out_info.show_separate_line()

    if input("\n Добавить в базу ? [ y(да) / n(нет) ]: ") == "y":
        database_set = SessionCreateSet(connect, music_struct.data)
        database_set.create_to_database()

        print("\n Данные добавлены !\n")

        if out_info.try_restart() != 'r':
            break
    else:
        break
