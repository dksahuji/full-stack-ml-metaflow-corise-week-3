import typer
import git
import os
from common_git_ops import write_gitignore_file, set_origin_to_users


def main(
    name: str,
    email: str,
    gh_account: str,
    repo_name: str = "full-stack-ml-metaflow-corise-week-1",
    branch_name: str = "main",
    gh_pat: str = None,
):

    os.chdir(os.path.join("/home/workspace/workspaces", repo_name))
    my_gh_repo_path = f"https://github.com/{gh_account}/{repo_name}"

    try:
        _ = os.listdir(".git")
        raise ValueError(
            f"""

There is already a .git directory at {os.path.join(os.getcwd(), '.git')}!
You can continue using it, or if you are confident you will not lose any work, then you can manually delete it with:

    rm -rf {os.path.join(os.getcwd(), '.git')}

You will either want to delete and recreate the empty repo at {my_gh_repo_path}, or instead of running this script, clone your existing repo:

    git clone {my_gh_repo_path}.git

"""
        )

    except FileNotFoundError as e:
        pass  # this is what we want.

    repo = git.Repo.init(".")
    with repo.config_writer() as git_config:
        git_config.set_value("user", "name", name)
        git_config.set_value("user", "email", email)
    write_gitignore_file()
    _git = repo.git
    _git.checkout(b=branch_name)
    _git.branch("-M", branch_name)
    _git.add(all=True)
    _git.commit(m="my first commit in corise workspace week 1!")
    set_origin_to_users(repo, my_gh_repo_path, gh_account, gh_pat)
    _git.push("--set-upstream", "origin", branch_name)

    print(
        "\nIf you made it this far with no errors, you should be ready to roll with all your favorite git commands for week 1!\n"
    )


if __name__ == "__main__":
    typer.run(main)
