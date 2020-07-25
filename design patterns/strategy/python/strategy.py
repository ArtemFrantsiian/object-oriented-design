import unittest
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """
    The Strategy interface declares operation common to all supported versions
    of sorting algorithm.
    """
    @abstractmethod
    def sort(self, l: List[int]) -> List[int]:
        pass


class MergeSort(Strategy):
    @staticmethod
    def merge(unsorted_values: List[int], left: List[int], right: List[int]):
        i = j = 0

        for k in range(0, len(unsorted_values)):
            if i == len(left):
                unsorted_values[k] = right[j]
                j = j + 1
                continue

            if j == len(right):
                unsorted_values[k] = left[i]
                i = i + 1
                continue

            if left[i] <= right[j]:
                unsorted_values[k] = left[i]
                i = i + 1
            else:
                unsorted_values[k] = right[j]
                j = j + 1

    def sort(self, l: List[int]) -> List[int]:
        p = 1
        r = len(l)
        if p >= r:
            return l

        q = (p + r) // 2
        left = self.sort(l[:q])
        right = self.sort(l[q:])
        self.merge(l, left, right)
        return l


class InsertionSort(Strategy):
    def sort(self, l: List[int]) -> List[int]:
        for i in range(1, len(l)):
            key = l[i]
            j = i - 1

            while j >= 0 and l[j] > key:
                l[j + 1] = l[j]
                j = j - 1

                l[j + 1] = key

        return l


class Context:
    """
    The Context defines the interface of interest to clients.
    """
    def __init__(self, strategy: Strategy) -> None:
        self._strategy: Strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def sort(self, l: List[int]) -> List[int]:
        return self._strategy.sort(l)


class TestMethods(unittest.TestCase):

    def test_1(self):
        ul = [3, 1, 2, 5, 4, 9, 7, 6, 8]
        context = Context(MergeSort())
        ol_ms = context.sort(ul)

        context.strategy = InsertionSort()
        ol_is = context.sort(ul)
        self.assertEqual(ol_ms, ol_is)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

