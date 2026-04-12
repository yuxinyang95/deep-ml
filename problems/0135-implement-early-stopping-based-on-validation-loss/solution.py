from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    if not val_losses:
        return None, None

    best_loss = val_losses[0]
    best_epoch = 0
    no_improve_count = 0

    for epoch in range(1, len(val_losses)):
        loss = val_losses[epoch]

        # 只有比历史最好再低超过 min_delta，才算 improvement
        if loss < best_loss - min_delta:
            best_loss = loss
            best_epoch = epoch
            no_improve_count = 0
        else:
            no_improve_count += 1

        if no_improve_count >= patience:
            return epoch, best_epoch

    return len(val_losses) - 1, best_epoch