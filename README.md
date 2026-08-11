# Sorting Algorithms: Bubble Sort vs Heap Sort

A modular Python project for implementing, testing, benchmarking, and
comparing **Bubble Sort** and **Heap Sort (Binary Heap)**.

The project evaluates both algorithms using the same randomly generated
datasets and measures their execution time across different dataset
sizes.

## Project Objectives

The project aims to:

-   Implement Bubble Sort.
-   Implement Heap Sort using a binary heap.
-   Generate reproducible random datasets.
-   Verify that both algorithms produce correctly sorted output.
-   Benchmark both algorithms using identical datasets.
-   Repeat experiments multiple times and calculate average execution
    time.
-   Save experimental results to CSV.
-   Generate a line graph comparing algorithm performance.
-   Provide a modular command-line interface using Click.
-   Provide automated tests using pytest.

## Algorithms

### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them when
they are in the wrong order.

  Case        Complexity
  --------- ------------
  Best              O(n)
  Average          O(n²)
  Worst            O(n²)

Bubble Sort is simple to understand and implement but becomes
inefficient for large datasets.

### Heap Sort

Heap Sort uses a binary heap data structure. For ascending sorting, a
max heap is constructed and the largest element is repeatedly moved to
the end of the dataset.

  Case        Complexity
  --------- ------------
  Best        O(n log n)
  Average     O(n log n)
  Worst       O(n log n)

Heap Sort therefore scales considerably better than Bubble Sort for
large datasets.

## Project Structure

``` text
sorting-algorithms/
│
├── tony_algorithms_sorter/
│   ├── __init__.py
│   ├── algorithms.py
│   ├── data.py
│   ├── benchmark.py
│   ├── csv_utils.py
│   └── cli.py
│
├── tests/
│   ├── test_algorithms.py
│   ├── test_data.py
│   └── test_benchmark.py
│
├── data/
│   └── datasets/
│
├── results/
│   ├── results.csv
│   └── sorting_performance.png
│
├── plot_results.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Requirements

The project requires:

-   Python 3.10 or newer
-   Click
-   pytest
-   Matplotlib

## Installation

Clone the repository and move into the project directory:

``` bash
git clone <your-github-repository-url>
cd sorting-algorithms
```

Install the project in editable mode:

``` bash
python -m pip install -e '.[test]'
```

The editable installation allows changes to the source code to be used
immediately without reinstalling the package.

## Command-Line Interface

The project uses **Click** to provide a command-line interface.

After installation, check the available options:

``` bash
sorting-benchmark --help
```

Expected output includes:

``` text
Usage: sorting-benchmark [OPTIONS]

  Benchmark Bubble Sort against Heap Sort.

Options:
  --repetitions INTEGER
  --seed INTEGER
  --help
```

### Run the benchmark

For the final experiment, five repetitions can be used:

``` bash
sorting-benchmark --repetitions 5 --seed 42
```

Alternatively, the module can be executed directly:

``` bash
python -m tony_algorithms_sorter.cli --repetitions 5 --seed 42
```

## Random Seed and Reproducibility

The `--seed` option controls the random-number generator.

For example:

``` bash
tony_algorithms_sorter --repetitions 5 --seed 42
```

Using the same seed allows the experiment to be reproduced with the same
generated datasets.

This is important because both algorithms must be tested using the same
input data for an **apple-to-apple comparison**.

The value `42` is not technically special; it is simply a fixed seed
chosen for reproducibility.

## Dataset Sizes

The benchmark evaluates the algorithms using:

-   1,000
-   5,000
-   15,000
-   20,000
-   25,000
-   30,000
-   35,000
-   40,000

For each dataset, Bubble Sort and Heap Sort operate on the same
generated values.

## Experimental Method

For each dataset size:

1.  Generate the dataset.
2.  Create a copy for each algorithm.
3.  Verify sorting correctness.
4.  Run Bubble Sort.
5.  Record execution time.
6.  Run Heap Sort.
7.  Record execution time.
8.  Repeat the experiment several times.
9.  Calculate the average runtime.
10. Save the results to CSV.

The same dataset is used for both algorithms to ensure a fair
comparison.

## Correctness Verification

Before performance measurements are considered, the sorting algorithms
are tested to ensure that they produce the expected sorted output.

Automated tests are provided using pytest.

Run all tests with:

``` bash
python -m pytest
```

The tests cover areas including:

-   Bubble Sort correctness.
-   Heap Sort correctness.
-   Empty datasets.
-   Small datasets.
-   Duplicate values.
-   Already sorted data.
-   Reverse-sorted data.
-   Dataset generation.
-   Benchmark functionality.

Correctness is checked before relying on the timing results so that
performance is not measured for an incorrect implementation.

## Benchmark Results

The benchmark stores experimental results in:

``` text
results/results.csv
```

The CSV contains the dataset size, algorithm, individual run times, and
average runtime.

Example structure:

``` text
dataset_size,algorithm,run_1_ms,run_2_ms,run_3_ms,run_4_ms,run_5_ms,average_ms
1000,Bubble Sort,...
1000,Heap Sort,...
5000,Bubble Sort,...
5000,Heap Sort,...
```

The average runtime is calculated from the repeated experiments.

## Plotting the Results

After the benchmark has completed, generate the performance graph with:

``` bash
python plot_results.py
```

The graph is saved as:

``` text
results/sorting_performance.png
```

The graph plots the average execution time against dataset size for both
algorithms.

The resulting line graph provides a visual comparison of how the
algorithms scale as the input size increases.

## Expected Findings

The experiment is expected to demonstrate that Bubble Sort becomes
increasingly expensive as the dataset size grows.

Bubble Sort has an average and worst-case complexity of:

``` text
O(n²)
```

Heap Sort has:

``` text
O(n log n)
```

Therefore, Heap Sort should demonstrate substantially better scalability
for the larger datasets.

In one experimental run with 40,000 elements, Bubble Sort took
approximately 76 seconds while Heap Sort took approximately 0.16
seconds. Exact timings may vary depending on the computer and system
load.

These experimental results support the theoretical complexity analysis.

## Why Multiple Repetitions?

Timing a program only once can be affected by temporary system activity
and other factors.

Running each experiment multiple times provides a more reliable
measurement.

The average is calculated as:

``` text
Average Time = (Run 1 + Run 2 + ... + Run n) / n
```

Five repetitions are recommended for the final experiment.

## Modular Design

The project separates different responsibilities into different modules.

### `algorithms.py`

Contains the sorting implementations:

-   Bubble Sort
-   Heap Sort

### `data.py`

Responsible for generating datasets.

### `benchmark.py`

Responsible for:

-   Running experiments.
-   Measuring execution time.
-   Repeating experiments.
-   Calculating averages.

### `csv_utils.py`

Responsible for:

-   Reading datasets.
-   Writing datasets.
-   Saving benchmark results.

### `cli.py`

Provides the Click command-line interface.

### `plot_results.py`

Reads benchmark results and generates the performance graph.

### `tests/`

Contains automated tests for the project.

This modular structure makes the application easier to test, maintain,
extend, and deploy.

## Example Workflow

A complete experiment can be performed using:

``` bash
# Install the project
python -m pip install -e '.[test]'

# Run tests
python -m pytest

# Run benchmark
sorting-benchmark --repetitions 5 --seed 42

# Generate graph
python plot_results.py
```

The resulting files are:

``` text
results/results.csv
results/sorting_performance.png
```

## GitHub Deployment

The project is structured so that it can be committed to and run from
GitHub.

A typical workflow is:

``` bash
git add .
git commit -m "Add sorting algorithm benchmark"
git push
```

Another user can then clone the repository and install it with:

``` bash
python -m pip install -e '.[test]'
```

and run:

``` bash
sorting-benchmark --repetitions 5 --seed 42
```

## References

Agarwal, B. (2022). *Hands-On Data Structures and Algorithms with
Python: Store, Manipulate, and Access Data Effectively and Boost the
Performance of Your Applications*. Packt Publishing.

Althoff, C. (2021). *The Self-Taught Computer Scientist: The Beginner's
Guide to Data Structures and Algorithms*. Wiley.

## License

This project is intended for educational and academic purposes.
