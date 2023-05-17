try:
    from datetime import datetime
    from metaflow import S3, Flow, namespace
    from metaflow.integrations import ArgoEvent
except ImportError:
    print("This script requires Metaflow version with Argo events.")
    exit(1)

namespace("")  # assume using default argo namespace, which is empty.
with S3(s3root="s3://outerbounds-datasets/taxi/") as s3:
    obj = s3.get("latest.parquet")
    last_s3_modification_event_time = datetime.fromtimestamp(obj.last_modified)
    run = Flow("TaxiFarePrediction").latest_run
    if run.created_at < last_s3_modification_event_time:
        ArgoEvent(name="s3").publish(force=True)
