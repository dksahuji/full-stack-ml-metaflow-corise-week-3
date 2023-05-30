def write_gitignore_file():
    contents = """.metaflow
metaflow_card_cache
__pycache__"""
    with open(".gitignore", "w") as f:
        f.write(contents)


def set_origin_to_users(repo, my_gh_repo_path, gh_account, gh_pat):
    for remote in repo.remotes:
        if remote.name == "origin":
            remote.rename("upstream")

    # Give your sandbox repository an 'origin' that points to your repository.
    # NOTE: This is why we need the gh_pat.
    # Make sure the PAT has access to only this repo.
    # Your sandbox should only need "Contents" read and write permission.
    url = my_gh_repo_path
    if gh_pat is not None:
        url = my_gh_repo_path.replace("https://", f"https://{gh_account}:{gh_pat}@")

    remote = repo.create_remote("origin", url=url)
    print(
        f"Renamed remote origin to upstream, and set {my_gh_repo_path} as origin url..."
    )
