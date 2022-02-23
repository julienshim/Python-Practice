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

# display options
for index, playlist in enumerate(playlists):
    option = f'{index + 1}. {playlist}'
    print(option)

selected_index = int(input(f'Select a playlist [1-{len(playlists)}]: ')) - 1
selected_playlist = playlists[selected_index]
print(selected_playlist)

# audio_files_path
audio_files_path = f'{getcwd()}/AUDIO/{selected_playlist.replace(".txt", "")}'
audio_files = listdir(audio_files_path)

# open and verify playlist
current_playlist = []
playlist_file_path = f'{getcwd()}/PLAYLIST/{selected_playlist}'
with open(playlist_file_path) as target_playlist:
    for track in target_playlist:
        track = track.strip()
        if track in audio_files:
            current_playlist.append(track)

def get_seconds_duration(track):
    audio = WAVE(f'./AUDIO/{track}')
    audio_info = audio.info
    length = int(audio_info.length)
    return length