from __future__ import annotations
import unittest
from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, element):
        pass


class ToArrayVisitor(Visitor):

    def visit(self, element):
        return [i.lower() for i in element.read()]


class ToSetVisitor(Visitor):

    def visit(self, element):
        return set([i.lower() for i in element.read()])


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def read(self):
        pass


class ConcreteElement(Element):

    def read(self):
        return "Component"

    def accept(self, visitor):
        return visitor.visit(self)


class TestMethods(unittest.TestCase):

    def test_1(self):
        element = ConcreteElement()
        res = element.accept(ToArrayVisitor())

        self.assertEqual(res, ["c", "o", "m", "p", "o", "n", "e", "n", "t"])

    def test_2(self):
        element = ConcreteElement()
        res = element.accept(ToSetVisitor())

        self.assertEqual(res, { "c", "o", "m", "p", "n", "e", "t" })


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)