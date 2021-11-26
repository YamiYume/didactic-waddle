from queue import LifoQueue, Empty, Full
from typing import Any, NoReturn


class StackLifoQueve:
    def __init__(self, size: int = 0) -> NoReturn:
        self._stack = LifoQueue(size)

    def isEmpty(self) -> bool:
        return self._stack.empty()

    def peek(self) -> Any:
        try:
            temporal = self._stack.get()
            self._stack.put(temporal)
            return temporal
        except Empty:
            pass

    def push(self, value: Any) -> NoReturn:
        try:
            self._stack.put(value)
        except Full:
            pass

    def pop(self) -> Any:
        try:
            return self._stack.get()
        except Empty:
            pass