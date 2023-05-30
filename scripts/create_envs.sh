#!/bin/bash

# set up dummy kaggle config to ease recsys notebook 1
# can reuse for any kaggle dataset download
mkdir ~/.kaggle
touch ~/.kaggle/kaggle.json
echo '{"username":"","key":""}' > ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

# activate to use in commands
. /home/workspace/mambaforge/etc/profile.d/conda.sh
. /home/workspace/mambaforge/etc/profile.d/mamba.sh

# create envs & enable in Jupyter
mamba env create -f /home/workspace/workspaces/tutorials/env.yml
mamba activate sandbox-tutorial
python -m ipykernel install --user --name sandbox-tutorial --display-name "Sandbox Onboarding Tutorial"

mamba env create -f /home/workspace/workspaces/original-metaflow-tutorial/env.yml
mamba activate original-metaflow-tutorial
python -m ipykernel install --user --name original-metaflow-tutorial --display-name "Original Metaflow Tutorial"

mamba env create -f /home/workspace/workspaces/intro-to-mf/env.yml
mamba activate intro-to-mf
python -m ipykernel install --user --name intro-to-mf --display-name "Intro to Metaflow"

mamba env create -f /home/workspace/workspaces/recsys/env.yml
mamba activate mf-tutorial-recsys
python -m ipykernel install --user --name mf-tutorial-recsys --display-name "Recsys Beginner Tutorial"

mamba env create -f /home/workspace/workspaces/nlp/env.yml
mamba activate mf-tutorial-nlp
python -m ipykernel install --user --name mf-tutorial-nlp --display-name "NLP Beginner Tutorial"

mamba env create -f /home/workspace/workspaces/cv/env.yml
mamba activate mf-tutorial-cv
python -m ipykernel install --user --name mf-tutorial-cv --display-name "CV Beginner Tutorial"

mamba env create -f /home/workspace/workspaces/cv-2/env.yml
mamba activate mf-tutorial-cv-2
python -m ipykernel install --user --name mf-tutorial-cv-2 --display-name "CV Intermediate Tutorial"

mamba env create -f /home/workspace/workspaces/full-stack-ML-metaflow-tutorial/env.yml
mamba activate full-stack-metaflow
python -m ipykernel install --user --name full-stack-metaflow --display-name "Full Stack ML Metaflow Tutorial"

mamba env create -f /home/workspace/workspaces/full-stack-ml-metaflow-corise-week-1/env.yml
mamba activate full-stack-metaflow-corise
python -m ipykernel install --user --name full-stack-metaflow-corise --display-name "Full Stack ML Corise"

mamba env create -f /home/workspace/workspaces/whisper/env.yml
mamba activate youtube-transcription
python -m ipykernel install --user --name youtube-transcription --display-name "Whisper Blog"

# make CLI ready to use
echo '# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/workspace/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/workspace/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/home/workspace/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/home/workspace/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/home/workspace/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/home/workspace/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<' >> ~/.bashrc
