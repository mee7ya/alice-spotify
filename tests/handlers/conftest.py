from typing import Dict, Any
from unittest.mock import Mock, MagicMock

import pytest

from tests.spotify_responses.current_user_playing_track import current_user_playing_track


@pytest.fixture
def current_song_mock_request() -> MagicMock:
    request: Mock = MagicMock()
    context = {
        'spotify_api': Mock()
    }

    request.app.__getitem__.side_effect = context.__getitem__
    return request


@pytest.fixture
def current_user_playing_track_response_none() -> None:
    return None


@pytest.fixture
def current_user_playing_track_response_not_playing() -> Dict[str, Any]:
    response: Dict[str, Any] = current_user_playing_track()
    response['is_playing'] = False
    return response


@pytest.fixture
def current_user_playing_track_response() -> Dict[str, Any]:
    return current_user_playing_track()
