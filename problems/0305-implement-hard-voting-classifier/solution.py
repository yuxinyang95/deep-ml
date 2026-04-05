from collections import Counter
def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    """
    Implement a hard voting classifier using majority vote.
    
    Args:
        predictions: 2D list where predictions[i][j] is classifier i's prediction for sample j
        
    Returns:
        List of final predictions using majority vote
    """
    result = []
    for pre in list(zip(*predictions)):
        c = Counter(pre)
        winner = sorted(c.items(), key=lambda x: (-x[1], x[0]))[0][0]
        result.append(winner)
    return result