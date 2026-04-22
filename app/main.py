import os.path

from console_out_info import ConsoleOutInfo
from music_type_struct import MusicTypeStruct
from app.database_level.session_create_set import SessionCreateSet

import time

connect = "postgresql://fluen:robov@localhost:5432/music_land_test"   # in env file


out_info = ConsoleOutInfo()
out_info.show_about_program()

while True:
    out_info.show_separate_line()

    input_data = out_info.enter_data()

    music_struct = MusicTypeStruct()

    start = time.time()   # speed test start
    music_struct.add_real_music_file(input_data)

    end = time.time() - start
    print(end)

    break

    # speed test point down
    # moving shadow 04.1 album -- buffer 4096 | single process
    # /home/fluenoriph/audio_files/[ASHADOW941CD] Moving Shadow 04.1 mixed By Timecode [2004]
    # 1. 0.6009175777435303
    # 2. 0.6131594181060791
    # 3. 0.6024560928344727
    # 4. 0.6069107055664062
    # 5. 0.6182007789611816

    # hash calc buffer = 65536
    # 1. 0.5713512897491455
    # 2. 0.5622050762176514
    # 3. 0.5635523796081543
    # 4. 0.5708482265472412
    # 5. 0.5720422267913818


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
