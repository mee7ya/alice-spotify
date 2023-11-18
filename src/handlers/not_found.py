from aiohttp import web

from src.chooser import chooser
from src.response import DialogsResponse


@chooser.register(not_found=True)
async def not_found_handler(request: web.Request):
    return DialogsResponse(
        text='К сожалению, я пока этого не умею',
        tts='К сожалению, я пока этого не умею',
    ).get_response()
