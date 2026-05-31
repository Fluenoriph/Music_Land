"""
* Music-Land CLI Utility *

Author: Ivan Bogdanov. All rights reserved
Date: June 2026 year
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru

--- Open-Source For Free ! ---

"""

import os.path
from dotenv import load_dotenv
import os
import typer
from cli_utility.console_out_info import ConsoleOutInfo
from cli_utility.all_files_searcher import AllFilesSearcher
from cli_utility.music_type_struct import MusicTypeStruct
from cli_utility.database_level.session_create_set import SessionCreateSet


class MusicCLIUtility:
    EXIT_MESSAGE = '\n Путь не существует !\n'
    APP = typer.Typer()
    MUSIC_STRUCT = MusicTypeStruct()
    OUT_INFO = ConsoleOutInfo()

    def __init__(self):
        MusicCLIUtility.APP()

    @staticmethod
    @APP.command()
    def sffi(path: str, directory: bool = False):
        if os.path.exists(path):
            if directory:
                MusicCLIUtility.MUSIC_STRUCT.add_real_some_music_files(AllFilesSearcher.find_all_files(path))
            else:
                MusicCLIUtility.MUSIC_STRUCT.add_real_one_music_file(path)

            print("\nНайдено:\n")
            MusicCLIUtility.OUT_INFO.show_audio_files_count(MusicCLIUtility.MUSIC_STRUCT.data)
            MusicCLIUtility.OUT_INFO.show_file_extract_data(MusicCLIUtility.MUSIC_STRUCT.data)

        else:
            typer.echo(MusicCLIUtility.EXIT_MESSAGE)
            return

    @staticmethod
    @APP.command()
    def wdb(path: str, directory: bool = False):
        if os.path.exists(path):
            if directory:
                MusicCLIUtility.MUSIC_STRUCT.add_real_some_music_files(AllFilesSearcher.find_all_files(path))
            else:
                MusicCLIUtility.MUSIC_STRUCT.add_real_one_music_file(path)

            load_dotenv()
            database_set = SessionCreateSet(os.getenv('DATABASE_URL'), MusicCLIUtility.MUSIC_STRUCT.data)
            database_set.create_to_database()   # If not errors !!  Exception ????

            print('\nДобавлено в базу данных:\n')
            MusicCLIUtility.OUT_INFO.show_audio_files_count(MusicCLIUtility.MUSIC_STRUCT.data)

        else:
            typer.echo(MusicCLIUtility.EXIT_MESSAGE)
            return


MusicCLIUtility()
