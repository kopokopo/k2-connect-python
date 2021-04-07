import unittest
import json
from unittest.mock import Mock
from tests import SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET


def mock_response(headers,
                  status_code,
                  content='CONTENT',
                  mock_json=None):

    # initialize mock response
    response = Mock()

    # define response content
    if isinstance(content, dict):
        response.content = json.dumps(content).encode('utf-8')
    else:
        response.content = bytes(content, 'utf-8')

    # define response headers
    response.headers = headers

    # define response status code
    response.status_code = status_code

    # define response json
    if mock_json:
        response.body = mock_json
        response.json = Mock(
            return_value=mock_json
        )
    return response


