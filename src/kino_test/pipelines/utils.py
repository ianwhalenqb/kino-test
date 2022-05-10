import os
import time
import logging
from typing import Callable
from functools import partial, update_wrapper


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
