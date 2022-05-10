"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from kino_test.pipelines import shmoys_lewis_example, no_dependencies_example


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    return {
        "__default__": shmoys_lewis_example.create_pipeline(),
        "no_deps": no_dependencies_example.create_pipeline(),
    }
