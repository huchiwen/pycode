def weighted_average(scores, weights):
    """
    Calculate the weighted average of a list of scores with corresponding weights.
    
    Args:
        scores (list): A list of numerical scores.
        weights (list): A list of numerical weights, with the same length as scores.
    
    Returns:
        The weighted average of the scores.
    """
    assert len(scores) == len(weights), "The number of scores must be equal to the number of weights."
    
    total_weighted_score = sum([score * weight for score, weight in zip(scores, weights)])
    total_weight = sum(weights)
    
    return total_weighted_score / total_weight

if __name__ == "__main__":
    
    s = [90, 85, 92, 88]
    w = [0.3, 0.2, 0.3, 0.2]

    result = weighted_average(s,w)
    print(result)
