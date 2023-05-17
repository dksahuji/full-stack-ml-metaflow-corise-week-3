import os
import json
import uuid
import time
from datetime import datetime

from metaflow import Metaflow, namespace, S3, metaflow_config

cfg = os.path.join(os.environ["HOME"], ".metaflowconfig", "config.json")
CONFIG = json.load(open(cfg))

STATE_FILE = "/tmp/.card_index.json"
HOUR = 3600
MAX_RUN_AGE = 4 * HOUR


def has_recent_runs():
    now = datetime.now()
    namespace(None)
    for flow in Metaflow():
        if (now - flow.latest_run.created_at).seconds < MAX_RUN_AGE:
            return True


def sync_cards(sync_status):
    with S3() as s3:
        objs = s3.list_recursive([metaflow_config.CARD_S3ROOT])
        for obj in objs:
            if "/steps/" in obj.key and obj.size > 0:
                if obj.key not in sync_status:
                    print("Syncing new card", obj.key, obj.size)
                    flow, _, run, _, step, _, task_id, _, _ = obj.key.split("/")
                    pathspec = f"{flow}/{run}/{step}/{task_id}"
                    card_id = str(uuid.uuid4()).replace("-", "")[:16]
                    public_url = (
                        os.path.join(CONFIG["METAFLOW_CARDS_S3_ROOT"], card_id)
                        + ".html"
                    )
                    id_prefix = CONFIG["METAFLOW_PUBLIC_CARD_INDEX"].split("/")[0]
                    card = s3.get(obj.url)
                    s3.put(public_url, card.blob, content_type="text/html")
                    yield (
                        obj.key,
                        {
                            "label": pathspec,
                            "id": os.path.join(id_prefix, card_id),
                            "tstamp": time.time(),
                        },
                    )


def load_index_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        print("no index file found")
        return {}


def store_index_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def upload_index(state):
    cards = list(sorted(state["sync_status"].values(), key=lambda x: x["tstamp"]))
    index = {"meta": {"type": "JSON_CARD_VIEWER"}, "data": cards}
    index_path = CONFIG["METAFLOW_PUBLIC_CARD_INDEX"].split("/")[-1]
    index_url = os.path.join(CONFIG["METAFLOW_CARDS_S3_ROOT"], index_path) + ".json"
    with S3() as s3:
        url = s3.put(index_url, json.dumps(index))
        print("updated index at", url)


def run_indexing():
    state = load_index_state()
    if "initialized" not in state:
        state.update({"initialized": True, "sync_status": {}})
        upload_index(state)
    if "sync_status" not in state:
        state["sync_status"] = {}
    updates = list(sync_cards(state["sync_status"]))
    state["sync_status"].update(updates)
    if updates:
        upload_index(state)
        store_index_state(state)


if __name__ == "__main__":
    if has_recent_runs():
        run_indexing()
