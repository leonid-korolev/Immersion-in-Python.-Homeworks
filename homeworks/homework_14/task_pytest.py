import pytest

from collections.abc import Hashable


def parameters_to_dict(**kwargs) -> dict:
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict


def test_parameters_to_dict():
    assert parameters_to_dict(a=1, b=2, c=3) == {1: 'a', 2: 'b', 3: 'c'}


def test_parameters_to_dict_not_hashed():
    assert parameters_to_dict(a=1, b=2, c=[3, 4]) == {1: 'a', 2: 'b', '[3, 4]': 'c'}


if __name__ == '__main__':
    pytest.main(['-v'])

