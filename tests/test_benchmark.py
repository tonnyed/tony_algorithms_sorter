"""Tests for benchmark functionality."""

from tony_algorithms_sorter.benchmark import (
    run_single_test,
    verify_result,
)


def test_verify_result():
    original = [5, 2, 8, 1]

    assert verify_result(
        original,
        [1, 2, 5, 8],
    )


def test_verify_result_fails():
    original = [5, 2, 8, 1]

    assert not verify_result(
        original,
        [5, 2, 8, 1],
    )


def test_single_benchmark():
    data = [64, 25, 12, 22, 11]

    bubble_time, heap_time = run_single_test(data)

    assert bubble_time >= 0
    assert heap_time >= 0