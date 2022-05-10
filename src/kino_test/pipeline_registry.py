"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from kino_test.pipelines import (
    new_toy_example,
    shmoys_lewis_example,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    return {"__default__": new_toy_example.create_pipeline()}
