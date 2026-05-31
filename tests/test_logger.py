from src.logger import log_message

def test_log_message(mocker):
    mocker.patch('src.logger.external_logger.send')
    mock_send = mocker.patch('src.logger.external_logger.send')
    log_message("hello")
    mock_send.assert_called_once_with("hello")