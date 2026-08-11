from pathlib import Path
import csv

import matplotlib.pyplot as plt


RESULTS_FILE = Path("results/results.csv")
GRAPH_FILE = Path("results/sorting_performance.png")


def load_results(filename):
    bubble = []
    heap = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row.get("average_ms"):
                continue

            dataset_size = int(row["dataset_size"])
            average = float(row["average_ms"])

            if row["algorithm"] == "Bubble Sort":
                bubble.append((dataset_size, average))

            elif row["algorithm"] == "Heap Sort":
                heap.append((dataset_size, average))

    bubble.sort()
    heap.sort()

    return bubble, heap


def create_plot(filename=RESULTS_FILE):
    GRAPH_FILE.parent.mkdir(parents=True, exist_ok=True)

    bubble, heap = load_results(filename)

    if not bubble:
        raise ValueError("No Bubble Sort results found.")

    if not heap:
        raise ValueError("No Heap Sort results found.")

    bubble_x = [item[0] for item in bubble]
    bubble_y = [item[1] for item in bubble]

    heap_x = [item[0] for item in heap]
    heap_y = [item[1] for item in heap]

    plt.figure(figsize=(10, 6))

    plt.plot(
        bubble_x,
        bubble_y,
        marker="o",
        label="Bubble Sort",
    )

    plt.plot(
        heap_x,
        heap_y,
        marker="o",
        label="Heap Sort",
    )

    plt.xlabel("Dataset Size")
    plt.ylabel("Average Runtime (ms)")
    plt.title("Bubble Sort vs Heap Sort Performance")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(GRAPH_FILE, dpi=300)
    plt.close()

    print(f"Graph saved to {GRAPH_FILE}")


if __name__ == "__main__":
    create_plot()