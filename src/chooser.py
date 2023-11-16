from typing import Dict, Any, Callable, Awaitable

from aiohttp import web

from src.handlers.welcome import welcome_handler
from src.handlers.not_found import not_found_handler


Handler = Callable[[web.Request, ], Awaitable[Any]]


class DialogsCommandChooser:
    def __init__(self, welcome_handler_: Handler, not_found_handler_: Handler):
        self.handlers: Dict[str, Handler] = {}
        self.welcome_handler: Handler = welcome_handler_
        self.not_found_handler: Handler = not_found_handler_

    def register(self, command: str):
        def decorator(handler: Handler):
            self.handlers[command.lower()] = handler
            return handler
        return decorator

    async def do_route(self, request: web.Request):
        if request.content_type != 'application/json':
            raise NotImplementedError(
                'Received wrong content_type. Only \'application/json\' is supported'
            )

        data: Dict[str, Any] = await request.json()

        command: str | None = next(iter(data['request']['nlu']['tokens']), None)
        if command is None:
            return await self.welcome_handler(request)

        handler: Handler | None = self.handlers.get(command)
        if handler is None:
            return await self.not_found_handler(request)

        return await handler(request)


chooser = DialogsCommandChooser(
    welcome_handler_=welcome_handler,
    not_found_handler_=not_found_handler,
)
