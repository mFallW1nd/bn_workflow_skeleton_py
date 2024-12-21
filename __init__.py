from binaryninja import *
from .workflow import register_workflow


name = "plugin.function.skeletonWorkflow"


def check_workflow_valid(view: BinaryView, func: Function):
    settings = Settings()
    return name in settings.query_property_string_list(
        "analysis.workflows.functionWorkflow",
        "enum",
    )


def plugin_command_action(view: BinaryView, func: Function):
    settings = Settings()

    current_workflow = settings.get_string("analysis.workflows.functionWorkflow", func)
    if current_workflow == name:
        target_workflow = "core.function.metaAnalysis"
    else:
        target_workflow = name

    settings.set_string("analysis.workflows.functionWorkflow", target_workflow, func)
    log_info(f"Set workflow <{target_workflow}> to function <{func.symbol.full_name}>")

    func.reanalyze()


register_workflow()
PluginCommand.register_for_function(
    "SkeletonWorkflow\\Toggle Workflow for Current Function",
    "",
    plugin_command_action,
    check_workflow_valid,
)
