from metaflow import Run, Flow, namespace
import pandas as pd
from typing import List, Dict
import os

namespace(None)


def check_success(flows: List[str]) -> bool:
    flow_runs = {}
    results = []
    for flow_name in flows:
        flow = Flow(flow_name)
        flow_runs[flow_name] = list(flow)
        for run in flow_runs[flow_name]:
            results.append(run.successful)
    return flow_runs, results


def write_flows_to_csv(
    flow_runs: Dict[str, List[Run]],
    file: str = "/home/workspace/scripts/tests/results.csv",
    workspace: str = None,
) -> None:
    df = {
        "flow": [],
        "run_id": [],
        "started_at": [],
        "finished_at": [],
        "success": [],
        "workspace": [],
    }
    for flow_name, runs in flow_runs.items():
        for run in runs:
            df["flow"].append(flow_name)
            df["run_id"].append(run.id)
            df["started_at"].append(run.created_at)
            df["finished_at"].append(run.finished_at)
            df["success"].append(run.successful)
            df["workspace"].append(workspace)
    if os.path.exists(file):
        old_df = pd.read_csv(file, index_col=0)
        df = pd.concat([old_df, pd.DataFrame(df)], ignore_index=True)
    else:
        df = pd.DataFrame(df)
    df["started_at"] = pd.to_datetime(df["started_at"])
    df["finished_at"] = pd.to_datetime(df["finished_at"])
    df.drop_duplicates(
        subset=["run_id", "flow", "workspace"], keep="last", inplace=True
    )
    df.sort_values(by="started_at", inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(file)
