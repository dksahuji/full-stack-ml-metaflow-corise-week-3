from utils import write_flows_to_csv, check_success
import numpy as np


def test_assert_all_flows_successful():
    flows = ["HelloFlow", "PlayListFlow", "MovieStatsFlow", "HelloCloudFlow"]
    flow_runs, runs_are_successful = check_success(flows)
    write_flows_to_csv(flow_runs, workspace="Metaflow OSS tutorial")
    assert not np.all(
        list(map(lambda x: "argo-moviestatsflow" in x, list(flow_runs.keys())))
    ), "Argo flow didn't run."
    assert np.all(runs_are_successful), "Not all flows were successful."
