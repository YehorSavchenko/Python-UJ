import pytest

from Zestaw9.SingleList import Node
from Zestaw9.SingleList import SingleList


def init_single_list():
    return SingleList()


def full_single_list():
    single_list = init_single_list()
    single_list.insert_tail(Node(3))
    single_list.insert_tail(Node(6))
    single_list.insert_tail(Node(8))
    return single_list


def test_init():
    assert (init_single_list().head is None)
    assert (init_single_list().tail is None)
    assert (init_single_list().length == 0)


def test_insert_head():
    single_list = init_single_list()
    single_list.insert_head(Node(5))
    assert (single_list.head.data == 5)
    assert (single_list.tail.data == 5)
    assert (single_list.length == 1)

    single_list.insert_head(Node(9))
    assert (single_list.head.data == 9)
    assert (single_list.tail.data == 5)
    assert (single_list.count() == 2)


def test_insert_tail():
    single_list = init_single_list()
    single_list.insert_tail(Node(5))
    assert (single_list.head.data == 5)
    assert (single_list.tail.data == 5)
    assert (single_list.length == 1)

    single_list.insert_tail(Node(9))
    assert (single_list.head.data == 5)
    assert (single_list.tail.data == 9)
    assert (single_list.count() == 2)


def test_remove_head():
    single_list = full_single_list()
    single_list.remove_head()
    assert (single_list.head.data == 6)
    assert (single_list.tail.data == 8)
    assert (single_list.count() == 2)

    single_list.remove_head()
    assert (single_list.head.data == 8)
    assert (single_list.tail.data == 8)
    assert (single_list.count() == 1)

    single_list.remove_head()
    assert (single_list.head is None)
    assert (single_list.tail is None)
    assert (single_list.count() == 0)


def test_search_in_list():
    single_list = full_single_list()
    assert (single_list.search(6).data == 6)
    assert (single_list.search(999) is None)


def test_find_min_in_list():
    single_list = init_single_list()
    assert (single_list.find_min() is None)

    single_list = full_single_list()
    assert (single_list.find_min().data == 3)


def test_find_max_in_list():
    single_list = init_single_list()
    assert (single_list.find_max() is None)

    single_list = full_single_list()
    assert (single_list.find_max().data == 8)


def test_reverse_list():
    single_list = init_single_list()
    single_list.reverse()
    assert single_list.is_empty()

    single_list = full_single_list()
    single_list.reverse()
    assert single_list.head.data == 8
    assert single_list.tail.data == 3


def test_is_empty():
    single_list = init_single_list()
    assert (single_list.is_empty())

    single_list = full_single_list()
    assert (not single_list.is_empty())


if __name__ == "__main__":
    pytest.main()
