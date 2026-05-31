'''
* Music-Land CLI Utility * Ivan Bogdanov. All rights reserved. 2026"

'''

import os.path
from dotenv import load_dotenv
import os
import typer
from cli_utility.console_out_info import ConsoleOutInfo
from cli_utility.all_files_searcher import AllFilesSearcher
from cli_utility.music_type_struct import MusicTypeStruct
from cli_utility.database_level.session_create_set import SessionCreateSet


load_dotenv()
connect_to_db = os.getenv('DATABASE_URL')

# /media/ripher12/samsung_ssd/ELECTRONICA/[ASHADOW941CD] Moving Shadow 04.1 mixed By Timecode [2004]
# /home/fluenoriph/music_test/media/ripher12/samsung_ssd/ELECTRONICA/[ASHADOW941CD] Moving Shadow 04.1 mixed By Timecode [2004]

app = typer.Typer()

@app.command()
def sffi(path: str, directory: bool = False):
    if os.path.exists(path):
        out_info = ConsoleOutInfo()
        music_struct = MusicTypeStruct()

        if directory:
            music_struct.add_real_some_music_files(AllFilesSearcher.find_all_files(path))

            out_info.show_finding_info(music_struct.data)
            out_info.show_file_extract_data(music_struct.data)
        else:
            music_struct.add_real_one_music_file(path)

            out_info.show_finding_info(music_struct.data)
            out_info.show_file_extract_data(music_struct.data)
    else:
        return


if __name__ == "__main__":
    app()

















    '''if input("\n Добавить в базу ? [ y(да) / n(нет) ]: ") == "y":
        database_set = SessionCreateSet(connect_to_db, music_struct.data)
        database_set.create_to_database()

        print("\n Данные добавлены !\n")

        if out_info.try_restart() != 'r':
            break
    else:
        break'''
