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

# functions

def filter_hidden(file_name):
    return not file_name.startswith(".")

def get_seconds_duration(track):
    audio = WAVE(f'./AUDIO/{selected_playlist.replace(".txt", "")}/{track}')
    audio_info = audio.info
    length = int(audio_info.length)
    return length

# settings
delay_between_audio = 1
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

with open(playlist_file_path) as target_playlist:
    for track in target_playlist:
        [order, track] = track.strip().split('\t')
        if track in audio_files:
            current_playlist.append((order, track))
        else:
            warnings.append(f'WARNING: MISSING{track}')

if len(audio_files) == len(current_playlist) and len(warnings) == 0:
    # total_duration_seconds
    total_duration_seconds = sum([get_seconds_duration(file_name) for (order, file_name) in current_playlist])
    total_duration_seconds = total_duration_seconds + (len(current_playlist) - 1) * delay_between_audio
    
    # total_duration hms
    total_duration_hms = timedelta(seconds=total_duration_seconds)

    # current time
    time_now = datetime.now()

    # estimated end time
    end_time = time_now + total_duration_hms

    # compensate for playback delay
    sleep(delay_at_beginning)

    # loop through playlist
    for (order, file_name) in current_playlist:
        # account for device setups with volume drift
        # call([f"osascript -e 'set volume output volume {volume_target}'"], shell=True)
        time_now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print('\t'.join(list(map(lambda i: str(i), [time_now, order, file_name]))))
        playsound(f'./AUDIO/{selected_playlist.replace(".txt", "")}/{file_name}')
        sleep(delay_between_audio)
else:
    print(f'Cannot play audio. {len(warnings)} warnings found: ')
    for index, warning in enumerate(warnings):
        print(f'{index+1}. {warning}')

