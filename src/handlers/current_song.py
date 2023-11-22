from typing import Dict, Any

import spotipy
from aiohttp import web

from src.chooser import chooser
from src.response import DialogsResponse


@chooser.register(command=r'(что (сейчас )?играет)|(какая (сейчас )?песня)')
async def current_song_handler(request: web.Request) -> web:
    spotify_api: spotipy.Spotify = request.app['spotify_api']

    data: Dict[str, Any] | None = spotify_api.current_user_playing_track()
    if data is not None and data['is_playing']:
        return DialogsResponse(
            text=f'Сейчас играет {data["item"]["name"]} от {data["item"]["artists"][0]["name"]}',
            tts=f'Сейчас играет {data["item"]["name"]} от {data["item"]["artists"][0]["name"]}',
        ).get_response()
    else:
        return DialogsResponse(
            text='Сейчас ничего не играет',
            tts='Сейчас ничего не играет',
        ).get_response()
