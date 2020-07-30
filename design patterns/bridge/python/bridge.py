from __future__ import annotations
import unittest
from abc import ABCMeta, abstractmethod


class Implementation(metaclass=ABCMeta):
    @abstractmethod
    def do_some_work(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def do_some_work(self) -> str:
        return "Concrete Implementation A"


class ConcreteImplementationB(Implementation):
    def do_some_work(self) -> str:
        return "Concrete Implementation B"


class Abstraction:
    def __init__(self, implementation: Implementation):
        self._implementation = implementation

    def do_some_work(self) -> str:
        return self._implementation.do_some_work()


class TestMethods(unittest.TestCase):

    def test_1(self):
        impl_a = ConcreteImplementationA()
        application = Abstraction(impl_a)

        self.assertEqual(application.do_some_work(), "Concrete Implementation A")

    def test_2(self):
        impl_b = ConcreteImplementationB()
        application = Abstraction(impl_b)

        self.assertEqual(application.do_some_work(), "Concrete Implementation B")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)