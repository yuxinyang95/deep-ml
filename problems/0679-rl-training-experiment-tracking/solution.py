import numpy as np

def track_rl_experiment(episode_rewards: list, episode_lengths: list, window_size: int = 10) -> dict:
    """
    Summarize metrics from an RL training run.
    
    Args:
        episode_rewards: Total reward per episode
        episode_lengths: Number of timesteps per episode
        window_size: Window size for moving average and improvement calculation
    
    Returns:
        Dictionary with training summary statistics
    """
    result = {}
    
    episode_rewards = np.asarray(episode_rewards, dtype=float)
    episode_lengths = np.asarray(episode_lengths, dtype=float)
    
    result["total_episodes"] = len(episode_rewards)
    result["mean_reward"] = round(np.mean(episode_rewards), 4)
    result["std_reward"] = round(np.std(episode_rewards), 4)
    result["max_reward"] = round(np.max(episode_rewards), 4)
    result["min_reward"] = round(np.min(episode_rewards), 4)
    
    result["best_episode"] = int(np.argmax(episode_rewards))
    result["mean_length"] = round(np.mean(episode_lengths), 4)
    
    w = min(window_size, len(episode_rewards))
    
    result["final_moving_avg"] = round(np.mean(episode_rewards[-w:]), 4)
    
    first_window_mean = np.mean(episode_rewards[:w])
    last_window_mean = np.mean(episode_rewards[-w:])
    result["reward_improvement"] = round(last_window_mean - first_window_mean, 4)
    
    return result
