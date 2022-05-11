"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from kino_test.pipelines import (
    shmoys_lewis_example,
    no_dependencies_example,
    new_toy_example,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    return {
        "__default__": shmoys_lewis_example.create_pipeline(),  # run with 3 jobs
        "no_deps": no_dependencies_example.create_pipeline(),  # run with 2 jobs
        "new_toy": new_toy_example.create_pipeline(),  # run with 3 jobs
    }
