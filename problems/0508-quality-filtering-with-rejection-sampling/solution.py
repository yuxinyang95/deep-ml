import numpy as np

def quality_filter_rejection_sampling(scores: list, threshold: float, n_select: int = None) -> dict:
    """
    Filter generated samples using quality-based rejection sampling.
    
    Args:
        scores: list of float quality scores for generated candidate samples
        threshold: minimum quality score required for acceptance
        n_select: optional maximum number of samples to return (top by score)
    
    Returns:
        dict with 'accepted_indices', 'acceptance_rate', 'mean_quality'
    """
    if not scores:
        return {
            "accepted_indices": [],
            "acceptance_rate": 0.0,
            "mean_quality": 0.0
        }

    # keep (score, index) for accepted samples
    clean = [(score, idx) for idx, score in enumerate(scores) if score >= threshold]

    # sort by score descending
    clean = sorted(clean, reverse=True)
    acceptance_rate = round(len(clean) / len(scores), 4)
    # apply optional top-k selection
    if n_select is not None:
        clean = clean[:n_select]

    accepted_indices = [idx for score, idx in clean]
    

    mean_quality = round(
        sum(score for score, idx in clean) / len(clean),
        4
    ) if clean else 0.0

    return {
        "accepted_indices": accepted_indices,
        "acceptance_rate": acceptance_rate,
        "mean_quality": mean_quality
    }