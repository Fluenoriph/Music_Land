from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.monkeysaudio import MonkeysAudio
from mutagen.wave import WAVE
from mutagen.musepack import Musepack
import mutagen


'''
APE, FLAC, M4A, MP3, MPC, WAV
-------------------------------
1. Тип файла
2. Имя файла
3. Размер файла
4. Путь файла
---------------
5. Заголовок
6. Исполнитель
7. Альбом
8. Название трека
9. Жанр
10. Год
11. Комментарий
------------------
12. Кодек
13. Битрейт
14. Частота дискретизации
15. Длительность

'''


flac_file = "D:\\ELECTRONICA\\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\\03 - Rascal & Klone - Winner Takes All.flac"
'''
audio_flac = FLAC(flac_file)

print(audio_flac.pprint())

print(audio_flac.info.bitrate)
print(audio_flac.info.sample_rate)
print(audio_flac.info.length)
'''

mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
audio_mp3 = MP3(mp3_file)
#print(audio_mp3.pprint())

#print(audio_mp3.info.bitrate)
#print(audio_mp3.info.sample_rate)
#print(audio_mp3.info.length)

ape = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
some_file = mutagen.File(r"D:\ELECTRONICA\Stim Axel - Сначала\Stim Axel - Сначала.ape")

print(some_file.pprint())

#print(some_file.info.bitrate)
print(some_file.info.sample_rate)
print(some_file.info.length)

audio_ape = MonkeysAudio(ape)
print(audio_ape.pprint())


