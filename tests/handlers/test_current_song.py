from typing import Dict, Any
from unittest.mock import MagicMock

import pytest
from pytest_lazy_fixtures import lf

from src.handlers import current_song_handler
from src.response import DialogsResponse


class TestCurrentSongHandler:
    @pytest.mark.parametrize(
        'spotify_response',
        [
            (lf('current_user_playing_track_response_none'), ),
            (lf('current_user_playing_track_response_not_playing'),),
        ]
    )
    async def test_not_playing(self, current_song_mock_request: MagicMock, spotify_response: Dict[str, Any] | None):
        current_song_mock_request.app['spotify_api'].current_user_playing_track.side_effect = spotify_response

        response = await current_song_handler(current_song_mock_request)
        assert DialogsResponse(
            text='Сейчас ничего не играет',
            tts='Сейчас ничего не играет',
        ).get_response().body == response.body
