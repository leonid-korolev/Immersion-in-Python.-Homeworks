import unittest
from collections.abc import Hashable


def param_to_dict(**kwargs) -> dict:
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict


class testParamToDict(unittest.TestCase):

    def test_input(self):
        self.assertEqual(param_to_dict(a=1, b=2, c=3), {1: 'a', 2: 'b', 3: 'c'})

    def test_not_hashed(self):
        self.assertEqual(param_to_dict(a=1, b=2, c=[3.4]), {1: 'a', 2: 'b', '[3, 4]': 'c'})


if __name__ == '__main__':
    unittest.main(verbosity=True)


