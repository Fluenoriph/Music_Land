from one_filetype_searcher import OneFileTypeSearcher
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.monkeysaudio import MonkeysAudio
from mutagen.wave import WAVE
from mutagen.musepack import Musepack


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








# High level classes >>>>

search_one_type = OneFileTypeSearcher(music_dir, MUSEPACK_TYPE)
search_one_type.separating_files_at_type()

#[print(file) for file in search_one_type.separated_files]
#print(len(search_one_type.separated_files))

for file in search_one_type.separated_files[0:100]:
    audio_info = Musepack(file)


    #info_list = audio_info.pprint().split('\n')

    inf = audio_info.info.version
    print(inf)
    #print(f"{audio_info.pprint()}\n")
    #print(audio_info.info.bitrate)








'''
more_type_searcher = MoreFileTypeSearcher(music_dir, music_file_types)
more_type_searcher.separating_files_at_type()

for f_type in music_file_types:
    file_type_sum = len(more_type_searcher.separated_files[f_type])

    print(f"{f_type} - [ {file_type_sum} ]")
'''









