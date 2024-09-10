import functools
import operator

from dflow import (
    Workflow,
)

from dpgen2.entrypoint.args import normalize as normalize_args
from dpgen2.entrypoint.common import (
    global_config_workflow,
)
from dpgen2.entrypoint.submit import (
    get_resubmit_keys,
)
from dpgen2.utils import (
    print_keys_in_nice_format,
)


def showkey(
    wf_id,
    wf_config,
):
    wf_config = normalize_args(wf_config)

    global_config_workflow(wf_config)

    wf = Workflow(id=wf_id)
    folded_keys = get_resubmit_keys(wf)
    all_step_keys = functools.reduce(operator.iadd, folded_keys.values(), [])
    prt_str = print_keys_in_nice_format(
        all_step_keys,
        ["run-train", "run-lmp", "run-fp", "diffcsp-gen", "run-relax"],
    )
    print(prt_str)  # noqa: T201
