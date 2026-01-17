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
4. Путь файла fullname
---------------
5. Название трека
6. Исполнитель
7. Альбом
8. Жанр
9. Год
------------------
Class >>>
12. Кодек
13. Информация о потоке, тип
13. Битрейт
14. Частота дискретизации
15. Разрядность
16. Длительность

'''


#flac_file = "D:\\ELECTRONICA\\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\\03 - Rascal & Klone - Winner Takes All.flac"
'''
audio_flac = FLAC(flac_file)

print(audio_flac.pprint())

print(audio_flac.info.bitrate)
print(audio_flac.info.sample_rate)
print(audio_flac.info.length)
'''

#mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
#audio_mp3 = MP3(mp3_file)
#print(audio_mp3.pprint())

#print(audio_mp3.info.bitrate)
#print(audio_mp3.info.sample_rate)
#print(audio_mp3.info.length)
'''


print(some_file.pprint())

#print(some_file.info.bitrate)
print(some_file.info.sample_rate)
print(some_file.info.length)
print(some_file.info.bits_per_sample)

audio_ape = MonkeysAudio(ape)
print(audio_ape.pprint())


mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
audio_mpc = mutagen.File(mpc_file)

print(audio_mpc.pprint())
print(audio_mpc.info.bitrate)
print(audio_mpc.info.sample_rate)
print(audio_mpc.info.length)
print(audio_mpc.info.bits_per_sample)


wav_file = r"D:\ELECTRONICA\Max Payne OST\American dream.wav"
audio_wav = mutagen.File(wav_file)
print(audio_wav.pprint())

print(audio_wav.info.bitrate)
print(audio_wav.info.sample_rate)
print(audio_wav.info.length)
print(audio_wav.info.bits_per_sample)

mp4_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"
audio_mp4 = MP4(mp4_file)
print(audio_mp4.pprint())

print(audio_mp4.info.bitrate)
print(audio_mp4.info.sample_rate)
print(audio_mp4.info.length)
print(audio_mp4.info.bits_per_sample)
'''

# ------------------------------------------------------------------------
flac_file = r"D:\ELECTRONICA\[2001] Various - Moving Shadow 01.1 (Mixed by Timecode)\03 - Rascal & Klone - Winner Takes All.flac"
mp3_file = r"D:\ELECTRONICA\-=INFINITI=- Drum & Bass Hard-Box vol.2\7. Tantrum Desire - Transformers.mp3"
ape = r"D:\ELECTRONICA\Ganja Kru - Super Sharp Shooter EP - ape\Various - DJ Hype Presents the Ganja Kru-Super Sharp Shooter EP.ape"
mpc_file = r"D:\ELECTRONICA\Easy Star All-Stars - Dub Side Of The Moon\10. Time Version.MPC"
wav_file = r"D:\ELECTRONICA\Miami Mix 2006 mixed by DJ Skorohott\WAV\07 Дорожка 7.wav"
m4a_file = r"D:\ELECTRONICA\Pendulum Discography [FLAC]\2006 - Jungle Sound Gold\16. Kingston Vampires.m4a"

for file in [flac_file, mp3_file, ape, mpc_file, wav_file, m4a_file]:
    audio_info = mutagen.File(file)
    print(f"{audio_info.pprint()}\n")

    #print(audio_info.info.bitrate) # not ape) _ / 1000 kbps/ round full

    #print(audio_info.info.sample_rate) # /1000. round full. kHz
    #print(audio_info.info.length) # / 60. round .2 minute

    #print(audio_info.info.bits_per_sample) # not mp3, mpc )) bit

#audio_info = mutagen.File(flac_file)

#info_list = audio_info.pprint().split('\n')

#print(info_list)










