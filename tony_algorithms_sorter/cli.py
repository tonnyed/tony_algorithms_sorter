"""Command-line interface for the sorting benchmark."""

from pathlib import Path

import click

from .benchmark import run_experiment
from .csv_utils import write_results


DATASET_SIZES = [
    1_000,
    5_000,
    15_000,
    20_000,
    25_000,
    30_000,
    35_000,
    40_000,
]


@click.command()
@click.option(
    "--repetitions",
    default=5,
    show_default=True,
    type=click.IntRange(min=1),
    help="Number of benchmark repetitions."
)
@click.option(
    "--seed",
    default=42,
    show_default=True,
    type=int,
    help="Random seed used to generate datasets."
)
def main(repetitions, seed):
    """Benchmark Bubble Sort against Heap Sort."""

    click.echo("")
    click.echo("=" * 60)
    click.echo("Bubble Sort vs Heap Sort Benchmark")
    click.echo("=" * 60)
    click.echo(f"Repetitions: {repetitions}")
    click.echo(f"Random seed: {seed}")
    click.echo("")

    results = []

    for size in DATASET_SIZES:

        click.echo(f"Dataset: {size:,}")

        result = run_experiment(
            size=size,
            repetitions=repetitions,
            seed=seed + size,
        )

        results.append(result)

        for run in range(repetitions):
            click.echo(
                f"  Run {run + 1}: "
                f"Bubble Sort = "
                f"{result['bubble_times'][run]:.3f} ms | "
                f"Heap Sort = "
                f"{result['heap_times'][run]:.3f} ms"
            )

        click.echo(
            f"  Average: "
            f"Bubble Sort = "
            f"{result['bubble_average']:.3f} ms | "
            f"Heap Sort = "
            f"{result['heap_average']:.3f} ms"
        )

        click.echo("")

    Path("results").mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = "results/results.csv"

    write_results(
        results,
        output_file,
    )

    click.echo("=" * 60)
    click.echo(f"Results saved to: {output_file}")
    click.echo("=" * 60)


if __name__ == "__main__":
    main()