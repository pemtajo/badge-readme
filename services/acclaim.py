from bs4 import BeautifulSoup
from yattag import Doc
import lxml, requests

from settings import ACCLAIM_SORT, ACCLAIM_USER, ACCLAIM_BASE_URL

class Acclaim:
    def __init__(self):
        self.BASE_URL = ACCLAIM_BASE_URL
        self.USER = ACCLAIM_USER
        self.SORT = ACCLAIM_SORT
    
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