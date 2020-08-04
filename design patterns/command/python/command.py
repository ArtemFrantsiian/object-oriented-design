from __future__ import annotations
import unittest
from abc import ABCMeta, abstractmethod


class Receiver:
    def operation(self, param: str) -> str:
        return f"Concrete Receiver operates command: {param}"


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> str:
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver, param: str):
        self._receiver = receiver
        self._param = param

    def execute(self) -> str:
        return self._receiver.operation(self._param)


class Sender:
    def __init__(self, command: Command):
        self._command = command

    def execute(self) -> str:
        return self._command.execute()


class TestMethods(unittest.TestCase):

    def test_1(self):
        param = "Concrete"
        receiver = Receiver()
        command = ConcreteCommand(receiver, param)
        sender = Sender(command)

        self.assertEqual(sender.execute(), f"Concrete Receiver operates command: {param}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)