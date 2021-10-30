import random
import json
import os


def create_random_dataset(
    # Starting with 1 billion data points
    data_points: int = 1_000_000_000,
    # ms-accuracy timestamp over a month
    max_value: int = 1000 * 60 * 60 * 24 * 31,
    # default
    filename: str = os.path.join("data", "random_points.json"),
):
    """
    Creates data_points random points between 0 and max_value and dumps them to filename

    Crashes my MacBook Air at the moment, only runs on my Linux desktop 😅

    Args:
        data_points: number of random data points to generate
        max_value: maximum value those data points can have
        filename: the file to dump the output to

    Returns:
        Nothing

    """
    print("Starting random dataset generation")

    random_points = []

    for i in range(data_points):
        if i * 100 % data_points == 0:
            print(f"{int(i/data_points*100)}% done")

        random_points.append(random.randint(0, max_value))

    print("Dumping data")

    with open(filename, "w+") as file:
        json.dump(random_points, file)
