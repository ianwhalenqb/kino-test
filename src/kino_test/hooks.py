"""
Kedro hooks.
"""

import logging
import time

from kedro.framework.hooks import hook_impl

logger = logging.getLogger(__name__)


class PipelineTimingHooks:
    """Hook for timing an entire pipeline.
    """
    def __init__(self):
        self.start = None

    @hook_impl
    def before_pipeline_run(self):
        """Start the pipeline timer.
        """
        self.start = time.time()

    @hook_impl
    def after_pipeline_run(self):
        """Log the pipeline runtime.
        """
        runtime = time.time() - self.start
        logger.log(logging.INFO, f"Pipeline runtime: {runtime:0.2f} seconds")


class NodeTimingHooks:
    @hook_impl
    def before_node_run(self, node, session_id):
        row = f"{node.name},{session_id},{time.time()}\n"

        with open("./start_times.csv", "a") as fptr:
            fptr.write(row)

    @hook_impl
    def after_node_run(self, node, session_id):
        row = f"{node.name},{session_id},{time.time()}\n"

        with open("./end_times.csv", "a") as fptr:
            fptr.write(row)
