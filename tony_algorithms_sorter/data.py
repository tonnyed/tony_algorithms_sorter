"""Dataset generation functions."""

import random


def generate_dataset(size, seed=None):
    """
    Generate a reproducible dataset of random integers.

    Args:
        size: Number of values to generate.
        seed: Optional random seed.

    Returns:
        A list of random integers.
    """
    rng = random.Random(seed)

    return [
        rng.randint(1, 100_000)
        for _ in range(size)
    ]