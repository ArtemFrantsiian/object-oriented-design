import unittest


class Component:
    def operation(self) -> str:
        return "Component"


class Decorator:
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ReverseOutput(Decorator):
    def operation(self) -> str:
        component = self.component.operation()
        res = [char.lower() for char in component]
        res.reverse()
        return "".join(res)


class TestMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(ReverseOutput(Component()).operation(), "tnenopmoc")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
