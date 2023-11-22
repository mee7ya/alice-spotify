from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest

from src.chooser import Handler


@web.middleware
async def content_type_middleware(request: web.Request, handler: Handler):
    if request.content_type != 'application/json':
        return HTTPBadRequest()

    return await handler(request)
