import unittest
from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class AbstractProductA(metaclass=ABCMeta):
    @abstractmethod
    def do(self) -> str:
        pass


class ProductAFactoryA(AbstractProductA):
    def do(self) -> str:
        return "Concrete Product A for Concrete Factory A"


class ProductAFactoryB(AbstractProductA):
    def do(self) -> str:
        return "Concrete Product A for Concrete Factory B"


class AbstractProductB(metaclass=ABCMeta):
    @abstractmethod
    def do_another(self) -> str:
        pass


class ProductBFactoryA(AbstractProductB):
    def do_another(self) -> str:
        return "Concrete Product B for Concrete Factory A"


class ProductBFactoryB(AbstractProductB):
    def do_another(self) -> str:
        return "Concrete Product B for Concrete Factory B"


class ConcreteFactoryA(AbstractFactory):
    def create_product_a(self):
        return ProductAFactoryA()

    def create_product_b(self):
        return ProductBFactoryA()


class ConcreteFactoryB(AbstractFactory):
    def create_product_a(self):
        return ProductAFactoryB()

    def create_product_b(self):
        return ProductBFactoryB()


class Application:
    def __init__(self, factory: AbstractFactory):
        self._factory = factory
        self._product_a = factory.create_product_a()
        self._product_b = factory.create_product_b()

    def do(self) -> str:
        return self._product_a.do()

    def do_another(self) -> str:
        return self._product_b.do_another()


class TestMethods(unittest.TestCase):

    def test_1(self):
        factory_a = ConcreteFactoryA()
        application = Application(factory_a)

        self.assertEqual(application.do(), "Concrete Product A for Concrete Factory A")

    def test_2(self):
        factory_a = ConcreteFactoryA()
        application = Application(factory_a)

        self.assertEqual(application.do_another(), "Concrete Product B for Concrete Factory A")

    def test_3(self):
        factory_b = ConcreteFactoryB()
        application = Application(factory_b)

        self.assertEqual(application.do(), "Concrete Product A for Concrete Factory B")

    def test_4(self):
        factory_b = ConcreteFactoryB()
        application = Application(factory_b)

        self.assertEqual(application.do_another(), "Concrete Product B for Concrete Factory B")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)