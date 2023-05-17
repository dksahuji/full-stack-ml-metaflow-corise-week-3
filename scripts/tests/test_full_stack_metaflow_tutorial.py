from utils import write_flows_to_csv, check_success
import numpy as np


def test_assert_all_flows_successful():
    flows = ["RF_Flow", "BSTFlow", "Branch_Flow", "NNFlow"]
    flow_runs, runs_are_successful = check_success(flows)
    write_flows_to_csv(flow_runs, workspace="Recsys beginner tutorial")
    assert np.all(runs_are_successful), "Not all flows were successful."
