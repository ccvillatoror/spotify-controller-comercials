import random
from pathlib import Path
from playsound3 import playsound

path = Path('media')

def play_comercial(file_name):
    playsound(file_name)

def choose_random_file():
    files = [str(f) for f in path.iterdir() if f.is_file()]
    random_file = random.choice(files)
    return random_file
