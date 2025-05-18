# for new replits please update the SPOTIFY_REDIRECT_URI to your repl url
# in this source code and the Spotify App oAuth2 redirect URI.

import os
from datetime import datetime

import spotipy
from flask import Flask, redirect, render_template, request, session, url_for
from spotipy.oauth2 import SpotifyOAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Constants
SPOTIFY_CLIENT_ID = os.environ.get('CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.environ.get(
    'SPOTIFY_REDIRECT_URI',
    'https://51bbd7ab-438d-4d02-bfb5-5459a39f72d3-00-2axuuvzb7pakf.spock.replit.dev/callback'
)
SCOPE = "user-read-recently-played user-top-read user-read-private"

# Get previous year for "top albums of last year" calculation
current_year = datetime.now().year
last_year = current_year - 1


@app.route('/')
@app.route('/<int:year>')
def index(year=None):
    # Check if user is authenticated
    if not session.get('token_info'):
        return render_template('login.html')

    # Get the Spotify client
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('login'))

    # Default to last year if no year is provided
    if year is None:
        year = last_year

    # Get top albums from the specified year
    top_albums = get_top_albums_of_year(sp, year)

    return render_template('index.html', albums=top_albums, year=year)


def get_top_albums_of_year(sp, year):
    # Calculate date range for the specified year
    results = sp.current_user_top_tracks(limit=50, time_range='medium_term')

    # Extract unique albums from top tracks
    albums = {}
    for item in results['items']:
        album = item['album']
        album_id = album['id']

        if album_id not in albums:
            album_release_date = album['release_date']
            # Only include albums released in the specified year
            if album_release_date.startswith(str(year)):
                albums[album_id] = {
                    'id': album_id,
                    'name': album['name'],
                    'artist': album['artists'][0]['name'],
                    'image_url':
                    album['images'][0]['url'] if album['images'] else None,
                    'release_date': album_release_date,
                    'spotify_url': album['external_urls']['spotify']
                }

    # If we don't have enough albums from user's top tracks, get popular albums from the specified year
    if len(albums) < 20:
        search_results = sp.search(q=f'year:{year}',
                                   type='album',
                                   market='US',
                                   limit=50 - len(albums))

        for album in search_results['albums']['items']:
            album_id = album['id']
            if album_id not in albums:
                albums[album_id] = {
                    'id': album_id,
                    'name': album['name'],
                    'artist': album['artists'][0]['name'],
                    'image_url':
                    album['images'][0]['url'] if album['images'] else None,
                    'release_date': album['release_date'],
                    'spotify_url': album['external_urls']['spotify']
                }

    return list(albums.values())


@app.route('/login')
def login():
    # Create SpotifyOAuth instance
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # Process the callback from Spotify
    sp_oauth = create_spotify_oauth()
    session.clear()

    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def create_spotify_oauth():
    return SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope=SCOPE)


def get_spotify_client():
    token_info = session.get('token_info', None)
    if not token_info:
        return None

    # Check if token expired and refresh if needed
    now = int(datetime.now().timestamp())
    is_expired = token_info['expires_at'] - now < 60

    if is_expired:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info

    return spotipy.Spotify(auth=token_info['access_token'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
