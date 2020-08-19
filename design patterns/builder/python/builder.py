from __future__ import annotations
import unittest
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass


class ConcreteBuilder(Builder):

    def __init__(self):
        self._product = Product()

    @property
    def product(self):
        return self._product

    def build_part_a(self):
        self._product.add("PartA")

    def build_part_b(self):
        self._product.add("PartB")

    def build_part_c(self):
        self._product.add("PartC")


class Product:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def __eq__(self, other):
        if not isinstance(other, list):
            return False
        return self._parts == other


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.build_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


class TestMethods(unittest.TestCase):

    def test_1(self):
        director = Director()
        director.builder = ConcreteBuilder()

        director.build_minimal_viable_product()

        self.assertEqual(director.builder.product, ["PartA"])

    def test_2(self):
        director = Director()
        director.builder = ConcreteBuilder()

        director.build_full_featured_product()

        self.assertEqual(director.builder.product, ["PartA", "PartB", "PartC"])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
