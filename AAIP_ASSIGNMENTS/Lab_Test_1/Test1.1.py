# Simple Stack implementation + unit tests

from typing import Generic, Iterable, List, Optional, TypeVar
import unittest

T = TypeVar("T")


class Stack(Generic[T]):
    """A simple LIFO stack with optional max_size and iterable init."""

    def __init__(self, iterable: Optional[Iterable[T]] = None, max_size: Optional[int] = None):
        if max_size is not None and max_size < 0:
            raise ValueError("max_size must be non-negative or None")
        self._items: List[T] = list(iterable) if iterable is not None else []
        self.max_size = max_size
        if self.max_size is not None and len(self._items) > self.max_size:
            raise OverflowError("Initial items exceed max_size")

    def push(self, item: T) -> None:
        """Push an item onto the stack. Raises OverflowError if full."""
        if self.max_size is not None and len(self._items) >= self.max_size:
            raise OverflowError("Stack has reached its max_size")
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item. Raises IndexError if empty."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it. Raises IndexError if empty."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def clear(self) -> None:
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r}, max_size={self.max_size!r})"
# Unit tests for edge cases and normal behavior
class TestStack(unittest.TestCase):
    def test_push_pop_peek(self):
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(len(s), 3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
    def test_peek_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()
    def test_max_size_overflow(self):
        s = Stack(max_size=2)
        s.push("a")
        s.push("b")
        with self.assertRaises(OverflowError):
            s.push("c")
    def test_init_from_iterable_and_order(self):
        s = Stack([1, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertEqual(s.pop(), 3)
    def test_init_exceeds_max_size(self):
        with self.assertRaises(OverflowError):
            Stack([1, 2, 3], max_size=2)
    def test_negative_max_size_raises(self):
        with self.assertRaises(ValueError):
            Stack(max_size=-1)
    def test_clear_and_repr(self):
        s = Stack([1, 2])
        s.clear()
        self.assertTrue(s.is_empty())
        self.assertIn("Stack", repr(s))
if __name__ == "__main__":
    # Run tests on Windows: python "c:\Users\vardh\OneDrive\Documents\AIPP LAB TEST\Lab_Test_1\Test_1.1.py"
    unittest.main(verbosity=2)
