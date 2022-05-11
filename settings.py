import os

START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"

REPOSITORY = os.getenv("<letgis>/<letgis>")
GH_TOKEN = os.getenv("-")
GH_API_URL = os.getenv("https://api.github.com")
COMMIT_MESSAGE = os.getenv("Updated README with new badges")
CREDLY_USER = os.getenv("<letgis>")
CREDLY_SORT = os.getenv("RECENT")

BADGE_SIZE = os.getenv("INPUT_BADGE_SIZE", '110')
try:
    NUMBER_LAST_BADGES = int(os.getenv("INPUT_NUMBER_LAST_BADGES"))
except:
    NUMBER_LAST_BADGES = 0

CREDLY_BASE_URL= "http://www.credly.com"

LIST_REGEX = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
