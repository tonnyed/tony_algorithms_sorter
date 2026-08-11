"""Tests for sorting algorithms."""

from tony_algorithms_sorter.algorithms import (
    bubble_sort,
    heap_sort,
)


def test_bubble_sort():
    data = [64, 25, 12, 22, 11, 90, 5]

    assert bubble_sort(data) == sorted(data)


def test_heap_sort():
    data = [64, 25, 12, 22, 11, 90, 5]

    assert heap_sort(data) == sorted(data)


def test_empty_list():
    assert bubble_sort([]) == []
    assert heap_sort([]) == []


def test_single_element():
    assert bubble_sort([10]) == [10]
    assert heap_sort([10]) == [10]


def test_reverse_order():
    data = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]

    assert bubble_sort(data) == expected
    assert heap_sort(data) == expected


def test_duplicate_values():
    data = [5, 2, 5, 1, 2, 8]

    assert bubble_sort(data) == sorted(data)
    assert heap_sort(data) == sorted(data)