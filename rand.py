"""
This module contains functions for generating random numbers
and filling arrays with random values using system commands.
"""

import subprocess


def random_array(arr):
    """
    Populates the given array with random numbers using the 'shuf' command.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The input array filled with random integers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
