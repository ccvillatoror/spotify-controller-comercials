import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials (change for a more secure hadeling)
client_id = ''
client_secret = ''
redirect_uri = 'http://127.0.0.1:3000'

# scopes for Remote control playback, Get Available Devices, Pause playback
SCOPEs = ['app-remote-control', 'user-read-playback-state', 'user-modify-playback-state']

auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=SCOPEs)
sp = spotipy.Spotify(auth_manager=auth_manager)

def pause_spotify():
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            sp.pause_playback(device['id'])

def resume_spotify():
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            sp.start_playback(device['id'])
