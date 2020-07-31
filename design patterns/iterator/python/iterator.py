from __future__ import annotations
import unittest
from collections.abc import Iterable, Iterator
from typing import List


class ReverseIterator(Iterator):
    def __init__(self, collection: StringList):
        self._collection = collection
        self._position = -1

    def __next__(self) -> str:
        try:
            value = self._collection[self._position]
            self._position -= 1
        except IndexError:
            raise StopIteration()

        return value


class StringList(Iterable):
    def __init__(self, collection: List[str]):
        self._collection = collection

    def __iter__(self) -> ReverseIterator:
        return ReverseIterator(self._collection)


class TestMethods(unittest.TestCase):

    def test_1(self):
        l = ["a", "b", "c"]
        sl = StringList(l)

        self.assertEqual(list(reversed(l)), list(sl))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)