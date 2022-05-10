"""
Implements the example problem from Shmoys Lewis as a pipeline.
"""

from functools import partial, update_wrapper
import logging
import os
import time
from typing import Callable

from kedro.pipeline import Pipeline, pipeline, node

logger = logging.getLogger(__name__)


def sleepy_node(sleep: float, *args) -> bool:
    """Simple test node that sleeps.

    Args:
        sleep: sleeping time in seconds.

    Returns:
        True.
    """
    msg = f"Node sleeping for {sleep} seconds on process with PID {os.getpid()}..."

    logger.log(logging.INFO, msg)

    time.sleep(sleep)

    return True


def partial_wrapper(func: Callable, *args, **kwargs) -> Callable:
    """Enables user to pass in arguments that are not datasets when function is called
    in a Kedro pipeline e.g. a string or int value.
    Args:
        func: Callable node function
     Returns:
        Callable
    """
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


def create_pipeline() -> Pipeline:
    return pipeline(
        [
            node(
                partial_wrapper(sleepy_node, 3),
                None,
                "output_1",
                name="job_1",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                None,
                "output_2",
                name="job_2",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                None,
                "output_3",
                name="job_3",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                ["output_1", "output_3"],
                "output_4",
                name="job_4",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                ["output_1", "output_2"],
                "output_5",
                name="job_5",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                "output_4",
                "output_6",
                name="job_6",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                None,
                "output_7",
                name="job_7",
            ),
        ]
    )
