import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	if data.ndim != 2:
		raise ValueError("The input is 2 dimension")
	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)
	standardized_data = np.where(std == 0, 0, (data - mean) / std)

	min_val = np.min(data, axis=0)
	max_val = np.max(data, axis=0)
	ranges = max_val - min_val
	normalized_data = np.where(ranges == 0, 0, (data - min_val)/ranges)
	return (np.round(standardized_data, 4), np.round(normalized_data, 4))