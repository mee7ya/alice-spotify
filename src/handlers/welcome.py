from aiohttp import web

from src.response import DialogsResponse


async def welcome_handler(request: web.Request):
    return DialogsResponse(
        text='Привет, я могу помочь управлять Spotify плеером',
        tts='Привет, я могу помочь управлять Spotify плеером',
    ).get_response()
