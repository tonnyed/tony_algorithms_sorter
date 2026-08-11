"""CSV utilities for datasets and benchmark results."""

import csv
from pathlib import Path


def write_dataset(data, filename):
    """Write a dataset to a CSV file."""

    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["value"])

        for value in data:
            writer.writerow([value])


def read_dataset(filename):
    """Read a dataset from a CSV file."""

    path = Path(filename)

    with path.open("r", newline="") as file:
        reader = csv.DictReader(file)

        return [
            int(row["value"])
            for row in reader
        ]


def write_results(results, filename):
    """Write benchmark results to a CSV file."""

    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    max_runs = 0

    for result in results:
        max_runs = max(
            max_runs,
            len(result["bubble_times"]),
            len(result["heap_times"]),
        )

    fieldnames = [
        "dataset_size",
        "algorithm",
    ]

    for run in range(1, max_runs + 1):
        fieldnames.append(f"run_{run}_ms")

    fieldnames.append("average_ms")

    with path.open("w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        for result in results:

            bubble_row = {
                "dataset_size": result["dataset_size"],
                "algorithm": "Bubble Sort",
                "average_ms": result["bubble_average"],
            }

            heap_row = {
                "dataset_size": result["dataset_size"],
                "algorithm": "Heap Sort",
                "average_ms": result["heap_average"],
            }

            for index, value in enumerate(
                    result["bubble_times"],
                    start=1,
            ):
                bubble_row[f"run_{index}_ms"] = value

            for index, value in enumerate(
                    result["heap_times"],
                    start=1,
            ):
                heap_row[f"run_{index}_ms"] = value

            writer.writerow(bubble_row)
            writer.writerow(heap_row)