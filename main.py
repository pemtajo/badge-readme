from bs4 import BeautifulSoup
import lxml, requests, json, re, os, sys, base64
from github import Github, GithubException

from yattag import Doc

START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"


REPOSITORY = os.getenv("INPUT_REPOSITORY")
GH_TOKEN = os.getenv("INPUT_GH_TOKEN")
COMMIT_MESSAGE = os.getenv("INPUT_COMMIT_MESSAGE")
ACCLAIM_USER = os.getenv("INPUT_ACCLAIM_USER")
ACCLAIM_SORT = os.getenv("INPUT_ACCLAIM_SORT")

class GithubRepo:
    def __init__(self, ghtoken, repository, commit_message):
        self.COMMIT_MESSAGE=commit_message
        g = Github(ghtoken)
        try:
            self.repo = g.get_repo(repository)
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

class Acclaim:
    def __init__(self, user, sort):
        self.BASE_URL = "http://www.youracclaim.com"
        self.USER = user
        self.SORT = sort
    
    def sort_by(self):
        return "most_popular" if self.SORT == 'POPULAR' else "-state_updated_at" 
        
    def convert_to_dict(self, htmlBadge):
        soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
        img = soupBadge.findAll("img", {"class": "cr-standard-grid-item-content__image"})[0]
        return {
            "title": htmlBadge["title"],
            "href": self.BASE_URL + htmlBadge["href"],
            "img": img["src"],
        }

    def return_badges_html(self):
        url = f"{self.BASE_URL}/users/{self.USER}/badges?sort={self.sort_by()}"
        response = requests.get(url)

        data = response.text
        soup = BeautifulSoup(data, "lxml")
        return soup.findAll("a", {"class": "cr-public-earned-badge-grid-item"})


    def generate_md_format(self, badges):
        doc, tag, text = Doc().tagtext()
        with tag("p", align="left"):
            for badge in badges:
                with tag("a", href=badge["href"], title=badge["title"]):
                    with tag("img", src=badge["img"], alt=badge["title"]):
                        text("")
        return doc.getvalue()
    
    def get_markdown(self):
        return self.generate_md_format([self.convert_to_dict(badge) for badge in self.return_badges_html()])

def generate_new_readme(md_badges, readme):
    """Generate a new Readme.md"""
    list_reg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
    badges_in_readme = f"{START_COMMENT}\n{md_badges}\n{END_COMMENT}"

    return re.sub(list_reg, badges_in_readme, readme)


if __name__ == "__main__":
    git = GithubRepo(GH_TOKEN, REPOSITORY, COMMIT_MESSAGE)
    acclaim_badges = Acclaim(ACCLAIM_USER, ACCLAIM_SORT)
    readme = git.get_readme()

    new_readme = generate_new_readme(acclaim_badges.get_markdown(), readme)
    if new_readme != readme:
        git.save_readme(new_readme)