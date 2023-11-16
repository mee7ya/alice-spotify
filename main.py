import os

import spotipy
from aiohttp import web
from dotenv import load_dotenv
from spotipy import SpotifyOAuth

from src.handlers import *
from src.chooser import chooser

if __name__ == '__main__':
    load_dotenv()

    spotify_api = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.environ['SPOTIFY_CLIENT_ID'],
            client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
            redirect_uri=os.environ['SPOTIFY_REDIRECT_URI'],
            scope='streaming app-remote-control user-read-currently-playing',
            open_browser=False,
        )
    )
    spotify_api.me()

    app = web.Application()
    app['spotify_api'] = spotify_api
    app.add_routes(
        [web.post(os.environ['SKILL_URL_PATH'], chooser.do_route)]
    )

    web.run_app(app=app)
