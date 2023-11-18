from typing import Dict, Any
from unittest.mock import AsyncMock, Mock

from src.chooser import chooser
from tests.utils import get_mock_request


class TestChooser:
    async def test_do_route(self, current_song_request: Dict[str, Any], play_song_request: Dict[str, Any]):
        current_song_handler: AsyncMock = AsyncMock()
        play_song_handler: AsyncMock = AsyncMock()

        chooser._handlers = {
            r'(что (сейчас )?играет)|(какая (сейчас )?песня)': current_song_handler,
            r'((включи)|(поставь)).*': play_song_handler,
        }

        request: Mock = get_mock_request(
            body=current_song_request
        )

        await chooser.do_route(request)
        current_song_handler.assert_called_once()

        request: Mock = get_mock_request(
            body=play_song_request
        )
        await chooser.do_route(request)
        play_song_handler.assert_called_once()
