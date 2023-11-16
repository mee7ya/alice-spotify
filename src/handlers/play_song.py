from typing import Any, Dict, List

import spotipy
from aiohttp.abc import Request

from src.chooser import chooser
from src.response import DialogsResponse


@chooser.register(command='включи')
async def play_song_handler(request: Request):
    spotify_api: spotipy.Spotify = request.app['spotify_api']

    data: Dict[str, Any] = await request.json()
    if len(data['request']['nlu']['tokens']) <= 1:
        return DialogsResponse(
            text='Не увидела название песни, которую вы хотите включить',
            tts='Не услышала название песни, которую вы хотите включить'
        ).get_response()

    song_data: List[str] = data['request']['nlu']['tokens'][1:]
    search_result: Dict[str, Any] = spotify_api.search(q=' '.join(song_data), type='track')

    found: bool = bool(search_result['tracks']['items'])
    if not found:
        return DialogsResponse(
            text='Не смогла найти песню по вашему запросу',
            tts='Не смогла найти песню по вашему запросу',
        ).get_response()

    song: Dict[str, Any] = search_result['tracks']['items'][0]
    artist_name: str = song['artists'][0]['name']
    song_name: str = song['name']
    song_uri: str = song['uri']
    album_uri: str = song['album']['uri']

    spotify_api.start_playback(context_uri=album_uri, offset={'uri': song_uri})

    return DialogsResponse(
        text=f'Включила {song_name} от {artist_name}',
        tts=f'Включила {song_name} от {artist_name}',
    ).get_response()
