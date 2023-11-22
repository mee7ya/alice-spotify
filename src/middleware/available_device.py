from typing import List, Dict, Any

import spotipy
from aiohttp import web

from src.chooser import Handler
from src.response import DialogsResponse


@web.middleware
async def available_device_middleware(request: web.Request, handler: Handler):
    spotify_api: spotipy.Spotify = request.app['spotify_api']

    devices: List[Dict[str, Any]] = spotify_api.devices()['devices']
    if not devices:
        return DialogsResponse(
            text='Нет подключенных устройств к Spotify. Пожалуйста, запустите приложение на одном из устройств',
            tts='Нет подключенных устройств к Spotify. Пожалуйста, запустите приложение на одном из устройств',
        )

    active_device = next((device for device in devices if device['is_active']), devices[0])
    request.app['active_device_id']: str = active_device['id']
    return await handler(request)
