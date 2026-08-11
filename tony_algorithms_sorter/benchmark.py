"""Benchmarking functionality for sorting algorithms."""

import time
from pathlib import Path

from .algorithms import bubble_sort, heap_sort
from .csv_utils import read_dataset, write_dataset
from .data import generate_dataset


def measure_sort(sort_function, data):
    """Measure sorting execution time in milliseconds.

    A fresh copy of the dataset is supplied to the sorting algorithm
    so that the original dataset remains unchanged.
    """
    values = data.copy()

    start = time.perf_counter()

    result = sort_function(values)

    elapsed_ms = (time.perf_counter() - start) * 1000

    return result, elapsed_ms


def verify_result(original, result):
    """Verify that result is the correctly sorted version of original."""
    return result == sorted(original)


def run_single_test(data):
    """Run both algorithms on identical input data.

    Each algorithm receives an independent copy of the same
    original dataset. This provides a fair comparison.
    """
    expected = sorted(data)

    bubble_result, bubble_time = measure_sort(
        bubble_sort,
        data,
    )

    if not verify_result(expected, bubble_result):
        raise AssertionError(
            "Bubble Sort produced an incorrect result."
        )

    heap_result, heap_time = measure_sort(
        heap_sort,
        data,
    )

    if not verify_result(expected, heap_result):
        raise AssertionError(
            "Heap Sort produced an incorrect result."
        )

    return bubble_time, heap_time


def benchmark_dataset(data, repetitions=5):
    """Benchmark both algorithms repeatedly on one dataset.

    This function is useful for unit testing and for smaller
    experimental datasets.

    Args:
        data: Dataset to sort.
        repetitions: Number of times each algorithm is executed.

    Returns:
        Dictionary containing individual timings and averages.
    """
    if repetitions < 1:
        raise ValueError("Repetitions must be at least 1.")

    bubble_times = []
    heap_times = []

    for _ in range(repetitions):
        bubble_time, heap_time = run_single_test(data)

        bubble_times.append(bubble_time)
        heap_times.append(heap_time)

    bubble_average = sum(bubble_times) / len(bubble_times)
    heap_average = sum(heap_times) / len(heap_times)

    return {
        "bubble_times": bubble_times,
        "heap_times": heap_times,
        "bubble_average_ms": bubble_average,
        "heap_average_ms": heap_average,
    }


def run_experiment(
        size,
        repetitions=5,
        seed=42,
        dataset_directory="data/datasets",
):
    """Run a complete benchmark for one dataset size.

    The dataset is generated once and reused for every repetition.
    Each sorting algorithm receives a fresh copy of the same dataset.

    Existing datasets are reused only when they contain exactly
    the requested number of elements. Empty or invalid datasets
    are automatically regenerated.

    Args:
        size: Number of elements in the dataset.
        repetitions: Number of benchmark repetitions.
        seed: Random seed used when generating the dataset.
        dataset_directory: Directory used to store datasets.

    Returns:
        Dictionary containing timings and averages.
    """
    if size <= 0:
        raise ValueError("Dataset size must be greater than zero.")

    if repetitions < 1:
        raise ValueError("Repetitions must be at least 1.")

    dataset_path = Path(dataset_directory)

    dataset_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataset_file = dataset_path / f"dataset_{size}.csv"

    # Attempt to load an existing dataset.
    try:
        data = read_dataset(str(dataset_file))

    except (FileNotFoundError, ValueError, TypeError):
        data = []

    # Generate a new dataset if necessary.
    if len(data) != size:
        data = generate_dataset(
            size,
            seed=seed,
        )

        write_dataset(
            data,
            str(dataset_file),
        )

    # Final validation before benchmarking.
    if len(data) != size:
        raise ValueError(
            f"Expected {size} elements, "
            f"but found {len(data)}."
        )

    bubble_times = []
    heap_times = []

    # Run the experiment multiple times.
    for _ in range(repetitions):
        bubble_time, heap_time = run_single_test(data)

        bubble_times.append(bubble_time)
        heap_times.append(heap_time)

    # Calculate arithmetic means.
    bubble_average = sum(bubble_times) / len(bubble_times)

    heap_average = sum(heap_times) / len(heap_times)

    return {
        "dataset_size": size,
        "bubble_times": bubble_times,
        "heap_times": heap_times,
        "bubble_average": bubble_average,
        "heap_average": heap_average,
    }