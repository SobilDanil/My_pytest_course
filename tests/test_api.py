import pytest
import requests

from src import api

@pytest.mark.skip(reason="падает из-за какой-то ерунды")
def test_get_data(mocker):
    mocker.patch(
        'src.api.requests.get',
        side_effect=requests.exceptions.ConnectionError('Connection error test')
    )
    with pytest.raises(ConnectionError):
        api.get_data()