from cameras import shutter_release as shoot, load_film as load, remove_film as eject  # noqa
from digital_camera import ask, trash

print(shoot())
print(load())
print(eject())

print(ask())
print(trash())
