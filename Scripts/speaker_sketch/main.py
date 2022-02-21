from os import listdir, getcwd
from playsound import playsound
from time import sleep
from datetime import datetime, timedelta
from re import findall
from mutagen.wave import WAVE
from subprocess import call

# settings
delay_between_audio = 30
delay_at_beginning = 5
volume_target = 75
playlists = [playlist for playlist in listdir(f'{getcwd()}/PLAYLIST')]
print(playlists)

def get_seconds_duration(track):
    audio = WAVE(f'./AUDIO/{track}')
    audio_info = audio.info
    length = int(audio_info.length)
    return length