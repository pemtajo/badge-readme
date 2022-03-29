import re
from settings import START_COMMENT, END_COMMENT, LIST_REGEX
from services.credly import Credly
from services.githubRepo import GithubRepo


def generate_new_readme(md_badges, readme):
    """Generate a new Readme.md"""
    if not md_badges:
        return readme
    badges_in_readme = f"{START_COMMENT}\n{md_badges}\n{END_COMMENT}"

    return re.sub(LIST_REGEX, badges_in_readme, readme)


if __name__ == "__main__":
    git = GithubRepo()
    credly_badges = Credly()
    readme = git.get_readme()

    new_readme = generate_new_readme(credly_badges.get_markdown(), readme)
    if new_readme != readme:
        git.save_readme(new_readme)
