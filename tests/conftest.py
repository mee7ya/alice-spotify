from typing import Any, Dict

import pytest

from tests.dialogs_requests.base_request import base_request


@pytest.fixture
def current_song_request() -> Dict[str, Any]:
    request: Dict[str, Any] = base_request()
    request['request']['command'] = 'что сейчас играет'
    return request


@pytest.fixture
def play_song_request() -> Dict[str, Any]:
    request: Dict[str, Any] = base_request()
    request['request']['command'] = 'поставь самую лучшую песню'
    return request
