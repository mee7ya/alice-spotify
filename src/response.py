from typing import Dict, Any

from aiohttp import web


class DialogsResponse:
    def _build_response(self) -> Dict[str, Any]:
        response: Dict[str, Any] = {
            'response': {},
            'version': self.version,
        }
        if self.text is not None:
            response['response']['text'] = self.text

        if self.tts is not None:
            response['response']['tts'] = self.tts

        return response

    def __init__(self, text: str | None = None, tts: str | None = None, version: str = '1.0') -> None:
        if text is None and tts is None:
            raise ValueError('Either text or tts have to be passed. Or both.')

        self.text: str | None = text
        self.tts: str | None = tts
        self.version: str | None = version

    def get_response(self) -> web.Response:
        return web.json_response(self._build_response())
