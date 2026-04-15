import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)
    folds = np.array_split(indices, k)
    result = []
    for i in range(k):
        predict = folds[i]
        train = np.concatenate([folds[j] for j in range(k) if i != j])
        result.append((train, predict))
    return result

        