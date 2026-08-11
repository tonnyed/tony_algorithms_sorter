"""Benchmarking functionality for sorting algorithms."""

import time

from .algorithms import bubble_sort, heap_sort
from .csv_utils import read_dataset, write_dataset


def measure_sort(sort_function, data):
    """Measure sorting execution time in milliseconds.

    A copy of the dataset is made so that the caller's original
    dataset is never modified by the sorting algorithm.
    """
    values = data.copy()

    start = time.perf_counter()

    result = sort_function(values)

    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000

    return result, elapsed_ms


def verify_result(original, result):
    """Verify that a sorting algorithm produced correct output."""
    return result == sorted(original)


def run_single_test(data):
    """Run both sorting algorithms on identical input data.

    Each algorithm receives an independent copy of the same
    original dataset, providing a fair apple-to-apple comparison.
    """
    expected = sorted(data)

    bubble_result, bubble_time = measure_sort(
        bubble_sort,
        data,
    )

    heap_result, heap_time = measure_sort(
        heap_sort,
        data,
    )

    if not verify_result(data, bubble_result):
        raise AssertionError(
            "Bubble Sort produced an incorrect result."
        )

    if not verify_result(data, heap_result):
        raise AssertionError(
            "Heap Sort produced an incorrect result."
        )

    return bubble_time, heap_time


def run_experiment(
        size,
        repetitions=5,
        seed=42,
        dataset_directory="data/datasets",
):
    """Run a benchmark for one dataset size.

    The dataset is generated once and reused for every repetition.
    Each sorting algorithm receives a fresh copy of that dataset.
    """

    dataset_file = (
        f"{dataset_directory}/dataset_{size}.csv"
    )

    try:
        data = read_dataset(dataset_file)

    except FileNotFoundError:
        from pathlib import Path

        Path(dataset_directory).mkdir(
            parents=True,
            exist_ok=True,
        )

        from .data import generate_dataset

        data = generate_dataset(
            size,
            seed=seed,
        )

        write_dataset(
            data,
            dataset_file,
        )

    bubble_times = []
    heap_times = []

    for _ in range(repetitions):
        bubble_time, heap_time = run_single_test(data)

        bubble_times.append(bubble_time)
        heap_times.append(heap_time)

    return {
        "dataset_size": size,
        "bubble_times": bubble_times,
        "heap_times": heap_times,
        "bubble_average": (
                sum(bubble_times) / len(bubble_times)
        ),
        "heap_average": (
                sum(heap_times) / len(heap_times)
        ),
    }