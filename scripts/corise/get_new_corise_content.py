import os
import sys
import git
import github
import typer
import configparser
from common_git_ops import write_gitignore_file, set_origin_to_users

COURSE_GH_ORG = "ob-ml-courses"


def try_reuse_name_and_email(repo):

    if os.path.exists("../full-stack-ml-metaflow-corise-week-1/.git"):
        week_1_repo = git.Repo("../full-stack-ml-metaflow-corise-week-1")
        with week_1_repo.config_reader() as git_config:
            try:
                name = git_config.get_value("user", "name")
                email = git_config.get_value("user", "email")
            except configparser.NoOptionError as e:
                print(
                    "Could not read user.name and user.email from week 1 repo... Type your response to the following prompts: \n"
                )
                name = typer.prompt(
                    "Please enter the name you want to use for git commits"
                )
                email = typer.prompt(
                    "Please enter the email you want to use for git commits"
                )
    else:
        print(
            "Could not find week 1 repo so cannot reuse user.name and user.email. Type your response to the following prompts: \n"
        )
        name = typer.prompt("Please enter the name you want to use for git commits")
        email = typer.prompt("Please enter the email you want to use for git commits")

    with repo.config_writer() as git_config:
        git_config.set_value("user", "name", name)
        git_config.set_value("user", "email", email)


def try_sync(week, gh_account, gh_pat=None):

    os.chdir("/home/workspace/workspaces")
    if gh_pat is not None:
        g = github.Github(gh_pat)
    else:
        g = github.Github()

    # Set paths for this week.
    repo_name = f"full-stack-ml-metaflow-corise-week-{week}"
    course_gh_repo_path = f"https://github.com/{COURSE_GH_ORG}/{repo_name}"
    sandbox_repo_path = f"/home/workspace/workspaces/{repo_name}"
    my_gh_repo_path = f"https://github.com/{gh_account}/{repo_name}"

    # Check ob-ml-courses has released the repo.
    try:
        # Throw github.GithubException if repo is empty.
        # Assume all empty repos are not-yet-released workspaces.
        repo_obj = g.get_repo(f"{COURSE_GH_ORG}/{repo_name}")
        contents = repo_obj.get_contents("")
    except github.GithubException as e:
        print(f"The content for week {week} is not released yet! 🧘 ⏳ 🧘")
        return

    # Check needed workspace files are present in ob-ml-courses repo.
    files = [f.path for f in contents]
    for f in ["workspace.code-workspace", ".obs-metadata.json"]:
        assert (
            f in files
        ), f"""
{f} is a needed workspace file not found in the {course_gh_repo_path} repository.
Please message us in the course channel!
"""

    # Check the user's gh_account has the repo created.
    try:
        _ = g.get_repo(f"{gh_account}/{repo_name}")
    except github.GithubException as e:
        sys.exit(
            f"""
Could not find your repository at {my_gh_repo_path}.
Before re-running this script, create an empty repository in your `{gh_account}` GitHub account with name {repo_name}.

You may also be trying to access a private repository. If this is the case, you need to pass a GitHub Personal Access Token (PAT) to this script:

    python /home/workspace/scripts/corise/get_new_corise_content.py \
        <GITHUB ACCOUNT NAME> --week <2, 3, or 4> --gh_pat <YOUR PAT>

Then, return to your sandbox and run `python /home/workspace/scripts/get_new_corise_content.py {gh_account}`.
"""
        )

    # Clone the repo from ob-ml-courses to your sandbox.
    try:
        repo = git.Repo.clone_from(course_gh_repo_path, sandbox_repo_path)
        os.chdir(sandbox_repo_path)
    except git.exc.GitCommandError as e:
        sys.exit(
            f"""
Encountered git.exc.GitCommandError when trying to clone the {course_gh_repo_path} repo to {sandbox_repo_path}.
Do you already have a repo at {sandbox_repo_path}?
If so, you should either `git pull` from that existing repository on your sandbox, or delete it and re-run this code.

WARNING: If you delete the {sandbox_repo_path} on your sandbox and have not downloaded your work to your laptop or pushed the workspace to GitHub, you will not be able to access that content any more!
If you are ok with this, you can delete with:

    rm -rf {sandbox_repo_path}
"""
        )

    # Configure sandbox repo to push to the user's github account.
    try:
        set_origin_to_users(repo, my_gh_repo_path, gh_account, gh_pat)
    except git.exc.GitCommandError as error:
        sys.exit(f"""Error changing remote from origin to upstream: {error}""")

    # Set email and name for git. This will prompt user if it cannot find email and name used for week 1 git commits.
    try_reuse_name_and_email(repo)

    # push files we want to user's remote repo.
    write_gitignore_file()
    repo.remotes.origin.push()

    # Set the tracking branch to point to repository in user's account.
    repo.heads.main.set_tracking_branch(repo.remotes.origin.refs.main)

    print(
        f"""
Your sandbox repo at {sandbox_repo_path} is synced,
    and the remote origin set to {my_gh_repo_path}.

To go to the workspace, after the `<UNIQUE>.dev/?workspace=/home/workspace/workspaces/` part of your sandbox URL, replace what is there with

    full-stack-ml-metaflow-corise-week-{week}/workspace.code-workspace

You can also save this URL which takes you directly to that workspace next time you want to login to your sandbox:
    https://account.outerbounds.dev/account/?workspace=/home/workspace/workspaces/full-stack-ml-metaflow-corise-week-{week}/workspace.code-workspace
"""
    )


def main(gh_account: str, week: str = "all", gh_pat: str = None):

    if week == "all":
        for week in [2, 3, 4]:
            try_sync(week, gh_account, gh_pat=gh_pat)
    else:
        week = int(week)
        assert week in [2, 3, 4], "Specify course week as `2`, `3`, or `4`."
        try_sync(week, gh_account, gh_pat=gh_pat)


if __name__ == "__main__":
    typer.run(main)
