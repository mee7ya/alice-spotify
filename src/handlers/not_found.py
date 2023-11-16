from aiohttp import web

from src.response import DialogsResponse


async def not_found_handler(request: web.Request):
    return DialogsResponse(
        text='К сожалению, я пока этого не умею',
        tts='К сожалению, я пока этого не умею',
    ).get_response()
