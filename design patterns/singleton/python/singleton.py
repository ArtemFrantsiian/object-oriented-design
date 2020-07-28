import unittest

class SingletonMeta(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


class TestMethods(unittest.TestCase):

    def test_1(self):
        in1 = Singleton()
        in2 = Singleton()

        self.assertEqual(in1, in2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)