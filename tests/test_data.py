"""Tests for dataset generation."""

from tony_algorithms_sorter.data import generate_dataset


def test_dataset_size():
    data = generate_dataset(100, seed=42)

    assert len(data) == 100


def test_dataset_reproducibility():
    data1 = generate_dataset(100, seed=42)
    data2 = generate_dataset(100, seed=42)

    assert data1 == data2


def test_dataset_values():
    data = generate_dataset(100, seed=42)

    assert all(
        1 <= value <= 100_000
        for value in data
    )