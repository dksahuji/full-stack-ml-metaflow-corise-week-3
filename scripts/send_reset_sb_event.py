#!/usr/bin/env python

import requests
from os.path import exists
from os import getenv
import json
from datetime import datetime, timezone

path_to_mf_config = "/home/workspace/.metaflowconfig/config.json"
analytics_id_field_name = "SANDBOX_CREATEDBY_ANALYTICS_ID"
heap_analytics_url = "https://heapanalytics.com/api/track"
heap_app_id_env_var = "HEAP_APPLICATION_ID"


def build_request_body(user_id, app_id):
    return json.dumps(
        {
            "app_id": app_id,
            "identity": user_id,
            "event": "reset-sandbox",
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        }
    )


def send_reset_sandbox_event():
    mf_config_exists = exists(path_to_mf_config)
    app_id = getenv(heap_app_id_env_var)
    if mf_config_exists and app_id is not None:
        with open(path_to_mf_config, "r") as f:
            try:
                analytics_id = json.loads(f.read())[analytics_id_field_name]
                payload = build_request_body(analytics_id, app_id)
                headers = {"Content-Type": "application/json"}
                requests.post(heap_analytics_url, headers=headers, data=payload)
            except KeyError:
                return


if __name__ == "__main__":
    send_reset_sandbox_event()
