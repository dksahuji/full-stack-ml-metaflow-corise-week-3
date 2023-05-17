#!/bin/bash

# activate mamba for use in bash script
. /home/workspace/mambaforge/etc/profile.d/mamba.sh

# sandbox onboarding tutorials
cd /home/workspace/workspaces/tutorials
mamba activate sandbox-tutorial
python hello/flow.py run
python branch/flow.py run
python versioning/flow.py run
python foreach/flow.py run
python scaling/flow.py run
python deps/flow.py --environment=conda --no-pylint run
python model/flow.py --environment=conda --no-pylint run

# metaflow.org oss tutorial
cd /home/workspace/workspaces/original-metaflow-tutorial
mamba activate original-metaflow-tutorial
python 00-helloworld/helloworld.py run
python 01-playlist/playlist.py run
jupyter nbconvert --to notebook --execute 01-playlist/playlist.ipynb
python 02-statistics/stats.py run
jupyter nbconvert --to notebook --execute 02-statistics/stats.ipynb
python 03-playlist-redux/playlist.py run
python 04-playlist-plus/playlist.py --environment=conda run
python 05-hello-cloud/hello-cloud.py run
jupyter nbconvert --to notebook --execute 05-hello-cloud/hello-cloud.ipynb
python /home/workspace/scripts/uncomment_decorator.py --file 02-statistics/stats.py --decorator conda_base
python 02-statistics/stats.py --environment conda run --with kubernetes --max-workers 4
jupyter nbconvert --to notebook --execute 06-statistics-redux/stats.ipynb
jupyter nbconvert --to notebook --execute 07-worldview/worldview.ipynb
python 02-statistics/stats.py --environment=conda --with kubernetes argo-workflows create --max-workers 4
python 02-statistics/stats.py --environment=conda argo-workflows trigger

# outerbounds.com intro to metaflow tutorial
cd /home/workspace/workspaces/intro-to-mf
mamba activate intro-to-mf
python season-1/minimum_flow.py run
python season-1/decorator_flow.py run
python season-1/artifact_flow.py run
jupyter nbconvert --to notebook --execute season-1/S1E3-analysis.ipynb
python season-1/parameter_flow.py run
python season-2/random_forest_flow.py run
python season-2/gradient_boosted_trees_flow.py run
python season-2/branching_trees_flow.py run
jupyter nbconvert --to notebook --execute season-2/S2E4-analysis.ipynb
python season-3/neural_net_flow.py run --e 2
python season-3/neural_net_card_flow.py run --e 2

# nlp beginner tutorial
cd /home/workspace/workspaces/nlp
mamba activate mf-tutorial-nlp
jupyter nbconvert --to notebook --execute nlp-1.ipynb
jupyter nbconvert --to notebook --execute nlp-2.ipynb
python baselineflow.py run
python branchflow.py run
python nlpflow.py run
jupyter nbconvert --to notebook --execute nlp-6.ipynb
python predflow.py run

# cv beginner tutorial
cd /home/workspace/workspaces/cv
mamba activate mf-tutorial-cv
jupyter nbconvert --to notebook --execute cv-intro-1.ipynb
jupyter nbconvert --to notebook --execute cv-intro-2.ipynb
python model_comparison_flow.py run --epochs 1
python tuning_flow.py run --epochs 1
jupyter nbconvert --to notebook --execute cv-intro-5.ipynb
python prediction_flow.py run --im './mnist_random_img.npy'

# recsys beginner tutorial
cd /home/workspace/workspaces/recsys
mamba activate mf-tutorial-recsys
mkdir ~/.kaggle
touch ~/.kaggle/kaggle.json
echo '{"username":"metaflowsandbox","key":"472cc922c3b7435a5bf8c79d670101db"}' > ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d andrewmvd/spotify-playlists
unzip -o spotify-playlists.zip
python clean_dataset.py
jupyter nbconvert --to notebook --execute recsys-1.ipynb
python data_flow.py run
python embed_and_model.py run
python recsys_tuning_flow.py run
jupyter nbconvert --to notebook --execute recsys-5.ipynb
python recsys_deploy.py run

# cv intermediate tutorial
cd /home/workspace/workspaces/cv-2
mamba activate mf-tutorial-cv-2
jupyter nbconvert --to notebook --execute cv-S2E1.ipynb
jupyter nbconvert --to notebook --execute cv-S2E2.ipynb
python classifier_flow.py run --epochs 1

# full stack ML metaflow tutorial
cd /home/workspace/workspaces/full-stack-ML-metaflow-tutorial
mamba activate full-stack-metaflow
python flows/local/rf_flow.py run
python flows/local/tree_branch_flow.py run
python flows/local/boosted_flow.py run
python flows/local/NN_flow.py run

# whisper
cd /home/workspace/workspaces/whisper
mamba activate youtube-transcription
python youtube_video_transcriber.py run --model 'tiny' --url 'https://www.youtube.com/watch?v=YQehg0uGBTY'
