def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    import numpy as np
    samples = np.asarray(samples)
    values, counts = np.unique(samples, return_counts=True)
    n = len(samples)

    return [(value, count / n) for value, count in zip(values, counts)]