"""
Implements the example problem from Shmoys Lewis as a pipeline.
"""

import logging
from kino_test.pipelines.utils import sleepy_node, partial_wrapper

from kedro.pipeline import Pipeline, pipeline, node

logger = logging.getLogger(__name__)


def create_pipeline() -> Pipeline:
    return pipeline(
        [
            node(
                partial_wrapper(sleepy_node, 3),
                None,
                "output_0",
                name="new_0",
            ),
            node(
                partial_wrapper(sleepy_node, 3),
                None,
                "output_1",
                name="new_1",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                None,
                "output_2",
                name="new_2",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                None,
                "output_3",
                name="new_3",
            ),
            node(
                partial_wrapper(sleepy_node, 1),
                ["output_1", "output_3"],
                "output_4",
                name="new_4",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                ["output_1", "output_2"],
                "output_5",
                name="new_5",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                "output_4",
                "output_6",
                name="new_6",
            ),
            node(
                partial_wrapper(sleepy_node, 15),
                None,
                "output_7",
                name="new_7",
            ),
            node(
                partial_wrapper(sleepy_node, 2),
                None,
                "output_8",
                name="new_8",
            ),
        ]
    )
