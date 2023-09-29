from unittest.mock import Mock
from lib.time_error import TimeError

def test_get_test_error_returns_difference_of_get_serve_time_and_time():
    requestor_mock = Mock()
    response_mock = Mock()
    time_mock = Mock()
    time_mock.time.return_value = 1695997516
    requestor_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1695997517}
    time_error = TimeError(requestor_mock, time_mock)
    assert time_error.error() == 1
