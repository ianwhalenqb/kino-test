"""
Implements the example problem with no dependencies.
"""

import logging

from kedro.pipeline import Pipeline, pipeline, node

from kino_test.pipelines.utils import sleepy_node, partial_wrapper

logger = logging.getLogger(__name__)


def create_pipeline() -> Pipeline:
    return pipeline(
        [
            node(
                partial_wrapper(sleepy_node, 3),
                None,
                "output_1",
                name="e_1",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                None,
                "output_2",
                name="e_2",
            ),
            node(
                partial_wrapper(sleepy_node, 3),
                None,
                "output_3",
                name="e_3",
            ),
            node(
                partial_wrapper(sleepy_node, 6),
                None,
                "output_4",
                name="e_4",
            ),
            node(
                partial_wrapper(sleepy_node, 4),
                None,
                "output_5",
                name="e_5",
            ),
            node(
                partial_wrapper(sleepy_node, 5),
                None,
                "output_6",
                name="e_6",
            ),
        ]
    )
