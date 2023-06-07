import pytest

from utils.dicts import get_val

# Тесты
def test_get_val():
    assert get_val({'1': 'hello'}, '1') == 'hello'
    assert get_val({'1': 'hello'}, '1', 'git') == 'hello'
    assert get_val({'1': 'hello'}, '3', 'ok') == 'ok'
    assert get_val({'1': 'hello'}, '3') == 'git'
