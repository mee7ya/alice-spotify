import re
from typing import Dict, Any, Callable, Awaitable

from aiohttp import web


Handler = Callable[[web.Request, ], Awaitable[web.Response]]


class DialogsCommandChooser:
    def __init__(self):
        self._handlers: Dict[str, Handler] = {}
        self._welcome_handler: Handler | None = None
        self._not_found_handler: Handler | None = None

    def register(self, command: str | None = None, welcome: bool = False, not_found: bool = False):
        def decorator(handler: Handler):
            if command is not None:
                self._handlers[command] = handler
                return handler

            if welcome:
                self._welcome_handler = handler
                return handler

            if not_found:
                self._not_found_handler = handler
                return handler

            raise ValueError(
                'None of the args (command, welcome, not_found) were passed. Can\'t register'
            )
        return decorator

    async def do_route(self, request: web.Request):
        data: Dict[str, Any] = await request.json()

        command: str = data['request']['command']
        if not command:
            return await self._welcome_handler(request)

        for _regex, _handler in self._handlers.items():
            if re.match(_regex, command):
                return await _handler(request)

        return await self._not_found_handler(request)


chooser = DialogsCommandChooser()
