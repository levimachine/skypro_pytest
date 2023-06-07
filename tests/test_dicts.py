import pytest

from utils.dicts import get_val


@pytest.fixture()
def return_dict():
    return {'1': 'hello'}


def test_get_val(return_dict):
    assert get_val(return_dict, '1') == 'hello'
    assert get_val(return_dict, '1', 'git') == 'hello'
    assert get_val(return_dict, '3', 'ok') == 'ok'
    assert get_val(return_dict, '3') == 'git'
