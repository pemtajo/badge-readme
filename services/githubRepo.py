from github import Github, GithubException

from settings import REPOSITORY, GH_TOKEN, GH_API_URL, COMMIT_MESSAGE
import sys, base64

class GithubRepo:
    def __init__(self):
        self.COMMIT_MESSAGE=COMMIT_MESSAGE

        # Automatic GitHub API detection.
        g = Github(base_url=GH_API_URL, login_or_token=GH_TOKEN)

        try:
            self.repo = g.get_repo(REPOSITORY)
        except GithubException:
            print(
                "Authentication Error. Try saving a GitHub Token in your Repo Secrets or Use the GitHub Actions Token, which is automatically used by the action."
            )
            sys.exit(1)
        try:
            self.contents_repo = self.repo.get_readme()
        except Exception:
            print(
                "The readme cannot be obtained!"
            )
            sys.exit(1)

    def save_readme(self, new_readme):
        self.repo.update_file(
            path=self.contents_repo.path, message=self.COMMIT_MESSAGE, content=new_readme, sha=self.contents_repo.sha
        )
    
    def get_readme(self):
        return str(base64.b64decode(self.contents_repo.content), "utf-8")
