from typing import Any, Dict
from unittest.mock import AsyncMock, Mock


def get_mock_request(body: Dict[str, Any], content_type: str = 'application/json') -> Mock():
    mock_request: Mock = Mock()
    mock_request.json = AsyncMock()

    if body:
        mock_request.json.return_value = body

    mock_request.content_type = content_type
    return mock_request
