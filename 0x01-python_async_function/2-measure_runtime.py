#!/usr/bin/env python3
"""
This module contains a function to measure the execution time of wait_n.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)

    Args:
        n (int): The number of wait_random calls.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n