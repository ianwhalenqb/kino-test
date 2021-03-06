"""
Implements the example problem from Shmoys Lewis as a pipeline.
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
