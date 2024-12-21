from .activity.skeleton import SkeletonActivity
from binaryninja import BinaryView, Workflow, log_info
import json

name = "plugin.function.skeletonWorkflow"
configuration = {
    "title": "SkeletonWorkflow",
    "description": "Skeleton Workflow for Python",
    "capabilities": [],
}


def register():
    workflow = Workflow().clone(name)

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
