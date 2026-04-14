def compute_inference_metrics(timestamps: list[float]) -> dict:
    """
    Compute LLM inference performance metrics from token timestamps.
    
    Args:
        timestamps: List of floats where timestamps[0] is the request start time
                    and timestamps[1:] are the times when each output token was generated.
    
    Returns:
        Dictionary with keys 'ttft', 'tps', 'itl' containing the metric values.
    """
    start = timestamps[0]
    first_token = timestamps[1]
    last_token = timestamps[-1]
    token_count = len(timestamps) - 1

    ttft = first_token - start
    tps = token_count / (last_token - start)

    if token_count == 1:
        itl = 0.0
    else:
        total_gap = 0.0
        for i in range(2, len(timestamps)):
            total_gap += timestamps[i] - timestamps[i - 1]
        itl = total_gap / (token_count - 1)

    return {
        "ttft": round(ttft, 4),
        "tps": round(tps, 4),
        "itl": round(itl, 4)
    }