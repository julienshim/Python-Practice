from os import listdir, getcwd
from playsound import playsound
from time import sleep
from datetime import datetime, timedelta
from re import findall
from mutagen.wave import WAVE
from subprocess import call


# sleep(15)
# test_tone = f"./TEST/1kHz_44100Hz_16bit_05sec.wav"
# playsound(test_tone)
# sleep(30)

def filter_hidden(file_name):
    return not file_name.startswith(".")

# settings
delay_between_audio = 30
delay_at_beginning = 5
# volume_target = 75
playlists = [playlist for playlist in listdir(f'{getcwd()}/PLAYLIST')]

# display options
for index, playlist in enumerate(playlists):
    option = f'{index + 1}. {playlist}'
    print(option)

selected_index = int(input(f'Select a playlist [1-{len(playlists)}]: ')) - 1
selected_playlist = playlists[selected_index]

# audio_files_path
audio_files_path = f'{getcwd()}/AUDIO/{selected_playlist.replace(".txt", "")}'
audio_files = list(filter(filter_hidden, listdir(audio_files_path)))

# open and verify playlist
current_playlist = []
warnings = []
playlist_file_path = f'{getcwd()}/PLAYLIST/{selected_playlist}'

def get_seconds_duration(track):
    audio = WAVE(f'./AUDIO/{selected_playlist.replace(".txt", "")}/{track}')
    audio_info = audio.info
    length = int(audio_info.length)
    return length

with open(playlist_file_path) as target_playlist:
    for track in target_playlist:
        [order, track] = track.strip().split('\t')
        print(track)
        if track in audio_files:
            current_playlist.append((order, track))
        else:
            warnings.append(f'WARNING: MISSING{track}')

print('audio files', audio_files)
print(len(current_playlist))

if len(audio_files) == len(current_playlist) and len(warnings) == 0:
    # total_duration_seconds
    print(selected_playlist)
    [play_order, track] = current_playlist[0]
    print(get_seconds_duration(track))
    # total_duration hms

    # current time

    # estimated time

    # compensate for playback delay

    # loop through playlist

    # account for device setups with volume drift
    # call([f"osascript -e 'set volume output volume {volume_target}'"], shell=True)
else:
    print(f'Cannot play audio. {len(warnings)} warnings found: ')
    for index, warning in enumerate(warnings):
        print(f'{index+1}. {warning}')

