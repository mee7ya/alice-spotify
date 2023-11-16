from aiohttp import web

from src.chooser import chooser
from src.response import DialogsResponse


@chooser.register(command='что')
async def current_song_handler(request: web.Request) -> web:
    spotify_api = request.app['spotify_api']
    data = spotify_api.current_user_playing_track()
    return DialogsResponse(
        text=f'Сейчас играет {data["item"]["name"]} от {data["item"]["artists"][0]["name"]}',
        tts=f'Сейчас играет {data["item"]["name"]} от {data["item"]["artists"][0]["name"]}',
    ).get_response()
