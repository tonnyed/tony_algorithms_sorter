"""Tests for benchmark functionality."""

from tony_algorithms_sorter.benchmark import (
    benchmark_dataset,
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


def test_verify_result_wrong_values():
    original = [5, 2, 8, 1]

    assert not verify_result(
        original,
        [1, 2, 5, 9],
    )


def test_verify_result_wrong_order():
    original = [5, 2, 8, 1]

    assert not verify_result(
        original,
        [8, 5, 2, 1],
    )


def test_verify_result_already_sorted():
    original = [1, 2, 5, 8]

    assert verify_result(
        original,
        [1, 2, 5, 8],
    )


def test_single_benchmark():
    data = [64, 25, 12, 22, 11]

    bubble_time, heap_time = run_single_test(data)

    assert bubble_time >= 0
    assert heap_time >= 0


def test_benchmark_dataset():
    data = [64, 25, 12, 22, 11]

    result = benchmark_dataset(
        data,
        repetitions=3,
    )

    assert len(result["bubble_times"]) == 3
    assert len(result["heap_times"]) == 3

    assert result["bubble_average_ms"] >= 0
    assert result["heap_average_ms"] >= 0