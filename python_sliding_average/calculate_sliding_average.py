from typing import List, Dict


# TODO Add a Cython and Numba test too
def calculate_sliding_average(
    data_points: List[int],
    sliding_average_minutes: 15,
) -> Dict[int, int]:
    """
    Creates a sliding average per minute for ms-accuracy events

    Args:
        data_points: list of integers representing ms-accuracy timestamps
        sliding_average_minutes: minutes to compute the sliding average on

    Returns:
        A list of integers representing the minutes and their sliding average, starting at 15 and ending at the
        last data point

    """
    ...
