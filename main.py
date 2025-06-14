import github
import fire
import dotenv
import tqdm

from github import GithubException


def is_empty_repo(client, repo_name):
    repo = client.get_repo(repo_name)
    try:
        repo.get_contents("/")
    except GithubException as e:
        message = e.args[1]['message']
        if e.status == 404 and message == "This repository is empty.":
            return True
    return False


def main(user_name: str, delete: bool = False):
    token = dotenv.get_key(".env", "GITHUB_TOKEN")
    if token is None or len(token) == 0:
        raise ValueError("GITHUB_TOKEN is not set in .env file")

    g = github.Github(token)
    user = g.get_user(user_name)
    repos = user.get_repos(type="all")

    for repo in tqdm.tqdm(list(repos), desc="Checking repositories"):
        if is_empty_repo(g, repo.full_name):
            print(f"Empty repository found: {repo.full_name}")
            if delete:
                try:
                    print(f"Deleting repository: {repo.full_name}")
                    repo.delete()
                except GithubException as e:
                    message = e.args[1]['message']
                    print(f"Failed to delete {repo.full_name}: {message}")


if __name__ == "__main__":
    fire.Fire(main)
