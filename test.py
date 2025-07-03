import pytest
from main import get_random_cat

def test_get_random_cat(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": "dm5",
        "url": "https://cdn2.thecatapi.com/images/dm5.jpg",
        "width": 3648,
        "height": 2736
    }

    cat_data = get_random_cat()
    assert cat_data['url'] == 'https://cdn2.thecatapi.com/images/dm5.jpg'


def test_get_random_cat_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_data = get_random_cat()
    assert cat_data is None
