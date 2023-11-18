from aiohttp import web

from src.chooser import chooser
from src.response import DialogsResponse


@chooser.register(welcome=True)
async def welcome_handler(request: web.Request):
    return DialogsResponse(
        text='Привет, я могу помочь управлять Spotify плеером',
        tts='Привет, я могу помочь управлять Spotify плеером',
    ).get_response()
