from src import utils

def test_utils_random(mocker):
    mocker.patch("src.utils.random.randint", return_value=42)
    assert utils.get_random_number() == 42