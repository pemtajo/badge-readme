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
USER = os.getenv("INPUT_ACCLAIM_USER", "pemtajo")


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


def open_readme():
    g = Github(ghtoken)
    try:
        repo = g.get_repo(repository)
    except GithubException:
        print(
            "Authentication Error. Try saving a GitHub Token in your Repo Secrets or Use the GitHub Actions Token, which is automatically used by the action."
        )
        sys.exit(1)
    return repo.get_readme()


def save_readme(md):
    with open("README.md", "w+") as file:
        file.write(md)


def generate_new_readme(badges: str, readme: str) -> str:
    """Generate a new Readme.md"""
    badges_in_readme = f"{START_COMMENT}\n{badges}\n{END_COMMENT}"
    return re.sub(list_reg, badges_in_readme, readme)


if __name__ == "__main__":
    badges = [convert_to_dict(badge) for badge in return_badges_html(USER)]
    # print(len(badges))
    # print(json.dumps(badges, indent=2))
    content = generate_md_format(badges)
    readme = open_readme()
    new_readme = generate_new_readme(content, readme)
    if new_readme != readme:
        save_readme(new_readme)
