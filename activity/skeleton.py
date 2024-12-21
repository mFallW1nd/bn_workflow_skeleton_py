import json
from binaryninja import Workflow, Activity, AnalysisContext, log_info


class SkeletonActivity(Activity):
    configuration = {
        "name": "skeleton.function.activitySkeleton",
        "title": "Activity Skeleton for Python",
        "description": "A skeleton activity for python",
        "eligibility": {
            "auto": {
                "default": False,
            },
        },
    }

    def __init__(self):
        super().__init__(json.dumps(self.configuration), action=self.run)

    def register(self, workflow: Workflow) -> str:
        workflow.register_activity(self)
        return self.configuration["name"]

    @staticmethod
    def run(context: AnalysisContext):
        log_info(
            f"Skeleton running for function: {hex(context.function.start)}"
            # Insert your logic here :P
        )
