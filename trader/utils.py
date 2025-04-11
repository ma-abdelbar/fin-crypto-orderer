# trader/utils.py

# Constants for BTCUSDT
TICK_SIZE = 0.1        # Minimum price increment
LOT_SIZE_STEP = 0.0001  # Minimum order quantity step


def snap2step(value: float, step: float) -> float:
    """
    Snap a float to the nearest valid step increment.
    Rounds to the nearest multiple of `step` with up to 8 decimal precision.
    """
    return round(round(value / step) * step, 8)
