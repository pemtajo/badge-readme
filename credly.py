from bs4 import BeautifulSoup
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from settings import (
    CREDLY_USER,
    NUMBER_LAST_BADGES,
)


class Credly:
    def __init__(self, username=None, number_badges=None, f=None):
        self.FILE = f
        self.BASE_URL = "https://www.credly.com"
        self.USER = username or CREDLY_USER or "kota.ogihara"
        self.NUMBER_BADGES = number_badges or NUMBER_LAST_BADGES or 0

        print(f"Credly scraper initialized for user: {self.USER}")

    def get_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        chrome_options.add_argument("--disable-renderer-backgrounding")
        chrome_options.add_argument("--disable-features=TranslateUI")
        chrome_options.add_argument("--disable-ipc-flooding-protection")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36")
        
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--silent")
        
        try:
            print("Setting up ChromeDriver using webdriver-manager...")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            print("ChromeDriver initialized successfully")
            return driver
        except Exception as e:
            print(f"Failed to initialize Chrome WebDriver: {e}")
            print("Trying fallback method without webdriver-manager...")
            try:
                driver = webdriver.Chrome(options=chrome_options)
                print("ChromeDriver initialized with fallback method")
                return driver
            except Exception as fallback_error:
                print(f"Fallback method also failed: {fallback_error}")
                raise

    def data_from_html(self):
        if self.FILE:
            with open(self.FILE, "r") as f:
                return f.read()
        
        url = f"{self.BASE_URL}/users/{self.USER}"
        print(f"Fetching data from: {url}")
        
        try:
            driver = self.get_webdriver()
            try:
                driver.get(url)
                
                print("Waiting for page to load...")
                WebDriverWait(driver, 15).until(
                    lambda d: d.find_element(By.ID, "root").get_attribute("innerHTML").strip() != ""
                )
                
                print("Page loaded, waiting for content to stabilize...")
                time.sleep(5)
                
                try:
                    see_all_button_selector = ".settings__skills-profile__edit-skills-profile__badge-list__see-all button"
                    see_all_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, see_all_button_selector))
                    )
                    
                    initial_badge_count = len(driver.find_elements(By.CSS_SELECTOR, "[class*='badge-card__card']"))
                    print(f"Initial badge count: {initial_badge_count}")

                    print("Found 'See all' button, clicking to expand badges...")
                    driver.execute_script("arguments[0].click();", see_all_button)
                    
                    WebDriverWait(driver, 15).until(
                        lambda d: len(d.find_elements(By.CSS_SELECTOR, "[class*='badge-card__card']")) > initial_badge_count or not d.find_elements(By.CSS_SELECTOR, see_all_button_selector)
                    )
                    
                    time.sleep(3)
                    
                    final_badge_count = len(driver.find_elements(By.CSS_SELECTOR, "[class*='badge-card__card']"))
                    print(f"Expanded badges. Final badge count: {final_badge_count}")

                except Exception as e:
                    print(f"Could not find or click 'See all' button, or no new badges loaded: {e}")

                print("Getting page source...")
                
                html_content = driver.page_source
                
                return html_content
            finally:
                driver.quit()
                
        except Exception as e:
            print(f"Selenium failed: {e}")
            print("Trying fallback method with requests...")
            
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
                }
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                html_content = response.text
                
                return html_content
                
            except Exception as fallback_error:
                print(f"Fallback method also failed: {fallback_error}")
                return None

    def convert_to_dict(self, htmlBadge):
        soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
        
        img = None
        possible_img_classes = [
            "settings__skills-profile__edit-skills-profile__badge-card__badge-image",
            "cr-standard-grid-item-content__image",
            "cr-public-earned-badge-grid-item__image",
            "badge-image",
            "cr-standard-grid-item-content__image"
        ]
        
        for img_class in possible_img_classes:
            imgs = soupBadge.find_all("img", {"class": img_class})
            if imgs:
                img = imgs[0]
                break
        
        if not img:
            img = soupBadge.find("img")
        
        if not img:
            return None
        
        title = ""
        title_element = soupBadge.find("div", {"class": lambda x: x and "organization-name-two-lines" in x})
        if title_element:
            title = title_element.get_text(strip=True)
        else:
            title = img.get("alt", "Badge")
        
        issuer = ""
        issuer_element = soupBadge.find("div", {"class": lambda x: x and "issuer-name-two-lines" in x})
        if issuer_element:
            issuer = issuer_element.get_text(strip=True)
        
        issue_date = ""
        issue_date_element = soupBadge.find("div", {"class": lambda x: x and "badge-card__issued" in x})
        if issue_date_element:
            date_text = issue_date_element.get_text(strip=True)
            import re
            date_match = re.search(r'(\d{2}/\d{2}/\d{2})', date_text)
            if date_match:
                issue_date = date_match.group(1)
        
        img_src = img.get("src", "")
        
        href = ""
        href_element = soupBadge.find("a", {"class": lambda x: x and "Cardstyles__StyledContainer-fredly__sc-1yaakoz-0" in x})
        if href_element and href_element.get("href"):
            href = self.BASE_URL + href_element["href"]
        else:
            href = f"{self.BASE_URL}/users/{self.USER}/badges"

        
        return {
            "title": title.replace('"', '\\"'),
            "img": img_src,
            "issuer": issuer,
            "issue_date": issue_date,
            "href": href
        }

    def return_badges_html(self):
        data = self.data_from_html()
        if not data:
            return []
            
        soup = BeautifulSoup(data, "lxml")
        
        badges = soup.find_all("div", {"class": lambda x: x and "badge-card__card" in x})
        
        if not badges:
            possible_badge_classes = [
                "cr-public-earned-badge-grid-item",
                "cr-earned-badge-grid-item",
                "badge-grid-item"
            ]
            
            for badge_class in possible_badge_classes:
                badges = soup.find_all("a", {"class": badge_class})
                if badges:
                    break
        
        if not badges:
            credly_images = soup.find_all('img', src=lambda x: x and 'images.credly.com' in x)
            if credly_images:
                print(f"Found {len(credly_images)} badges using image search")
                badges = [img.find_parent() or img for img in credly_images]
        
        print(f"Found {len(badges)} badge elements in HTML")
        return badges

    def generate_md_format(self, badges):
        if not badges:
            return None
        
        valid_badges = [badge for badge in badges if badge is not None]
        if not valid_badges:
            return None
            
        return "\n".join(
            map(
                lambda it: f"[![{it['title']}]({it['img']})]({it['href']} \"{it['title']}\")",
                valid_badges,
            )
        )

    def get_markdown(self):
        badges_html = self.return_badges_html()
        
        if self.NUMBER_BADGES > 0:
            badges_html = badges_html[:self.NUMBER_BADGES]
        
        badge_dicts = []
        for badge in badges_html:
            badge_dict = self.convert_to_dict(badge)
            if badge_dict:
                badge_dicts.append(badge_dict)
        
        def parse_date(date_str):
            if not date_str:
                return None
            try:
                day, month, year = date_str.split('/')
                year = '20' + year if int(year) < 50 else '19' + year
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except:
                return None
        
        print("\nExtracted badge dates:")
        for badge in badge_dicts:
            print(f"  {badge['title']}: {badge.get('issue_date', 'No date')}")
        
        badge_dicts.sort(key=lambda x: parse_date(x.get('issue_date', '')) or '1900-01-01', reverse=True)
        
        print("\nSorted badges (newest first):")
        for badge in badge_dicts:
            print(f"  {badge['title']}: {badge.get('issue_date', 'No date')}")
        
        return self.generate_md_format(badge_dicts)

    def save_markdown_to_file(self, filename="badges.md"):
        markdown = self.get_markdown()
        if markdown:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"Markdown saved to: {filename}")
            return True
        else:
            print("No markdown generated - check if badges were found")
            return False


def main():
    print("Testing Credly scraper...")
    
    credly = Credly()
    
    print(f"Fetching badges for user: {credly.USER}")
    print(f"Number of badges: {credly.NUMBER_BADGES}")
    
    markdown = credly.get_markdown()
    
    if markdown:
        print("\nGenerated markdown (sorted by issue date - newest first):")
        print(markdown)
    else:
        print("No markdown generated - check if badges were found")
    
    return markdown


if __name__ == "__main__":
    main()
