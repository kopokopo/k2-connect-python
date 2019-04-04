import unittest
from unittest.mock import Mock
from tests import SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET


def mock_response(headers,
                  status_code,
                  content='CONTENT',
                  json=None):

    # initialize mock response
    response = Mock()

    # define response content
    response.content = bytes(content)

    # define response headers
    response.headers = headers

    # define response status code
    response.status_code = status_code

    # define response json
    if json:
        response.json = Mock(
            return_value=json
        )
    return response


