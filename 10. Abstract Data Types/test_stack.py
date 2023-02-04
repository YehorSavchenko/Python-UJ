import pytest

from Zestaw10.Stack import Stack


def test_init():
    stack = Stack()
    assert stack.size == 10

    stack = Stack(5)
    assert stack.size == 5


def test_push():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    assert stack.n == 3


def test_pop():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    assert stack.pop() == 6
    assert stack.pop() == 4


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(3)
    assert not stack.is_empty()


def test_is_full():
    stack = Stack(3)
    stack.push(2)
    stack.push(4)
    assert not stack.is_full()
    stack.push(6)
    assert stack.is_full()


if __name__ == "__main__":
    pytest.main()
