from bs4 import BeautifulSoup
import lxml
import requests, json, re, os, sys, base64
from github import Github, GithubException

BASE_URL = "http://www.youracclaim.com"

from yattag import Doc

START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"
list_reg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

repository = os.getenv("INPUT_REPOSITORY")
ghtoken = os.getenv("INPUT_GH_TOKEN")
commit_message = os.getenv("INPUT_COMMIT_MESSAGE")
USER = os.getenv("INPUT_ACCLAIM_USER")


def convert_to_dict(htmlBadge):
    soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
    img = soupBadge.findAll("img", {"class": "cr-standard-grid-item-content__image"})[0]
    return {
        "title": htmlBadge["title"],
        "href": BASE_URL + htmlBadge["href"],
        "img": img["src"],
    }


def return_badges_html(user):
    url = BASE_URL + "/users/" + user + "/badges?sort=-state_updated_at"
    response = requests.get(url)

    data = response.text
    soup = BeautifulSoup(data, "lxml")
    return soup.findAll("a", {"class": "cr-public-earned-badge-grid-item"})


def generate_md_format(badges):
    doc, tag, text = Doc().tagtext()
    with tag("p", align="left"):
        for badge in badges:
            with tag("a", href=badge["href"], title=badge["title"]):
                with tag("img", src=badge["img"], alt=badge["title"]):
                    text("")
    return doc.getvalue()


def decode_readme(data: str) -> str:
    """Decode the contents of old readme"""
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, "utf-8")


def get_repo():
    g = Github(ghtoken)
    try:
        repo = g.get_repo(repository)
    except GithubException:
        print(
            "Authentication Error. Try saving a GitHub Token in your Repo Secrets or Use the GitHub Actions Token, which is automatically used by the action."
        )
        sys.exit(1)
    return repo


def open_readme(repo):
    return repo.get_readme()


def save_readme(repo, contents, new_readme):
    repo.update_file(
        path=contents.path, message=commit_message, content=new_readme, sha=contents.sha
    )


def generate_new_readme(md_badges, readme):
    """Generate a new Readme.md"""
    badges_in_readme = f"{START_COMMENT}\n{md_badges}\n{END_COMMENT}"
    return re.sub(list_reg, badges_in_readme, readme)


if __name__ == "__main__":
    repo = get_repo()
    md_badges = generate_md_format(
        [convert_to_dict(badge) for badge in return_badges_html(USER)]
    )

    contents_repo = open_readme(repo)
    readme = decode_readme(contents_repo.content)
    new_readme = generate_new_readme(md_badges, readme)

    if new_readme != readme:
        save_readme(repo, contents_repo, new_readme)
