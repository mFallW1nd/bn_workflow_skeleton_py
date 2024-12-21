from .activity.skeleton import SkeletonActivity
from binaryninja import BinaryView, Workflow, log_info
import json

name = "skeleton.function.skeletonWorkflow"
configuration = {
    "title": "SkeletonWorkflow",
    "description": "Skeleton Workflow for Python",
    "capabilities": [],
}


def register_workflow():
    workflow = Workflow("core.function.metaAnalysis").clone(name)

    # LLIL
    workflow.insert(
        "core.function.generateMediumLevelIL",
        [
            # ...
        ],
    )

    # MLIL
    workflow.insert(
        "core.function.generateHighLevelIL",
        [
            SkeletonActivity().register(workflow)
            # ...
        ],
    )

    workflow.register(json.dumps(configuration))
