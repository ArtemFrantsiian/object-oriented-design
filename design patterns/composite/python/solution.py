from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component) -> None:
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_folder(self) -> bool:
        return False

    @abstractmethod
    def open(self) -> str:
        pass


class Folder(Component):
    """
    Composite pattern
    """
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_folder(self) -> bool:
        return True

    def open(self) -> str:
        res = []
        for c in self._children:
            res.append(c.open())

        return f"Folder({'+'.join(res)})"


class File(Component):
    def open(self) -> str:
        return "File"


if __name__ == '__main__':
    root = Folder()
    root.add(File())

    folder1 = Folder()
    folder1.add(File())
    folder1.add(File())

    folder2 = Folder()
    folder2.add(File())

    root.add(folder1)
    root.add(folder2)

    tree = root.open()
    print(tree)
