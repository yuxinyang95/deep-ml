def early_stopping(val_losses: list[float], patience: int = 5, min_delta: float = 0.0) -> list[bool]:
	"""
	Determine at each epoch whether training should stop based on validation loss.
	
	Args:
		val_losses: List of validation losses at each epoch
		patience: Number of epochs to wait for improvement before stopping
		min_delta: Minimum change in validation loss to qualify as improvement
	
	Returns:
		List of booleans indicating whether to stop at each epoch
	"""
	# Your code here
	result = [False] * len(val_losses)
	best = val_losses[0]
	count = 0
	for idx, val in enumerate(val_losses[1:]):
		if val < best - min_delta:
			best = val
			count = 0
		else:
			count += 1
			if count >= patience:
				result[idx + 1] = True
	return result
		