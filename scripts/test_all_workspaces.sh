cd /home/workspace/workspaces/tutorials
mamba activate sandbox-tutorial
pytest /home/workspace/scripts/tests/test_sandbox_tutorials_results.py

cd /home/workspace/workspaces/original-metaflow-tutorial
mamba activate original-metaflow-tutorial
pytest /home/workspace/scripts/tests/test_metaflow_oss_tutorial.py

cd /home/workspace/workspaces/intro-to-mf
mamba activate intro-to-mf
pytest /home/workspace/scripts/tests/test_ob_intro_mf_tutorial.py

cd /home/workspace/workspaces/nlp
mamba activate mf-tutorial-nlp
pytest /home/workspace/scripts/tests/test_nlp_beginner_tutorial.py

cd /home/workspace/workspaces/cv
mamba activate mf-tutorial-cv
pytest /home/workspace/scripts/tests/test_cv_beginner_tutorial.py

cd /home/workspace/workspaces/recsys
mamba activate mf-tutorial-recsys
pytest /home/workspace/scripts/tests/test_recsys_beginner_tutorial.py

cd /home/workspace/workspaces/cv-2
mamba activate mf-tutorial-cv-2
pytest /home/workspace/scripts/tests/test_cv_intermediate_tutorial.py

cd /home/workspace/workspaces/full-stack-ML-metaflow-tutorial
mamba activate full-stack-metaflow
pytest /home/workspace/scripts/tests/test_full_stack_metaflow_tutorial.py

cd /home/workspace/workspaces/whisper
mamba activate youtube-transcription
pytest /home/workspace/scripts/tests/test_whisper_blog.py
