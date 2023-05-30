#!/bin/bash
. /home/workspace/mambaforge/etc/profile.d/mamba.sh
cd /home/workspace/workspaces/recsys
mamba activate mf-tutorial-recsys
while true
do
    python data_flow.py run
    python embed_and_model.py run
    python recsys_tuning_flow.py run
    python recsys_deploy.py run
done
