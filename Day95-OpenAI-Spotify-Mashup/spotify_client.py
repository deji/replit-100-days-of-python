import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client():
    """Initialize and return the Spotify client"""
    # Constants for Spotify API
    SPOTIFY_CLIENT_ID = os.environ.get('CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = os.environ.get(
        'SPOTIFY_REDIRECT_URI',
        'http://localhost:8080'
    )
    SCOPE = "user-read-private user-read-playback-state user-modify-playback-state"

    # Create SpotifyOAuth object
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )

    # Create Spotify client
    return spotipy.Spotify(auth_manager=auth_manager)

def search_track(client, query, limit=1):
    """Search for a track on Spotify"""
    results = client.search(q=query, type='track', limit=limit)
    
    if not results['tracks']['items']:
        return None
        
    track = results['tracks']['items'][0]
    return {
        'name': track['name'],
        'artist': track['artists'][0]['name'],
        'preview_url': track['preview_url'],
        'spotify_url': track['external_urls']['spotify']
    }