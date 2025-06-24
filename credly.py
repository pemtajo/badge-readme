from bs4 import BeautifulSoup
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import (
    CREDLY_SORT,
    CREDLY_USER,
    CREDLY_BASE_URL,
    BADGE_SIZE,
    NUMBER_LAST_BADGES,
)


class Credly:
    def __init__(self, username=None, sort_order=None, badge_size=None, number_badges=None, f=None):
        self.FILE = f
        self.BASE_URL = "https://www.credly.com"  # Updated to https
        self.USER = username or CREDLY_USER or "pemtajo"
        self.SORT = sort_order or CREDLY_SORT or "RECENT"
        self.BADGE_SIZE = badge_size or BADGE_SIZE or "80"
        self.NUMBER_BADGES = number_badges or NUMBER_LAST_BADGES or 0

        print(f"Credly scraper initialized for user: {self.USER}")

    def get_webdriver(self):
        """Initialize Chrome WebDriver with headless options"""
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
        
        # Add logging to debug issues
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--silent")
        
        try:
            return webdriver.Chrome(options=chrome_options)
        except Exception as e:
            print(f"Failed to initialize Chrome WebDriver: {e}")
            raise

    def data_from_html(self):
        """Get HTML content from Credly profile page using Selenium"""
        if self.FILE:
            with open(self.FILE, "r") as f:
                return f.read()
        
        url = f"{self.BASE_URL}/users/{self.USER}"
        print(f"Fetching data from: {url}")
        
        # Try Selenium first
        try:
            driver = self.get_webdriver()
            try:
                driver.get(url)
                
                # Wait for the React app to initialize (look for the root element to have content)
                print("Waiting for page to load...")
                WebDriverWait(driver, 15).until(
                    lambda d: d.find_element(By.ID, "root").get_attribute("innerHTML").strip() != ""
                )
                
                # Additional wait for JavaScript to fully render
                print("Page loaded, waiting for content to stabilize...")
                time.sleep(5)
                
                # Try to find badges, but don't fail if they're not there yet
                try:
                    badges = driver.find_elements(By.CSS_SELECTOR, "[class*='badge'], [class*='cr-'], [href*='/badges/']")
                    print(f"Found {len(badges)} potential badge elements")
                except:
                    print("No badge elements found yet, proceeding anyway...")
                
                print("Getting page source...")
                
                html_content = driver.page_source
                
                # Save HTML content to file for debugging
                filename = f"credly_html_{self.USER}.html"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(html_content)
                print(f"HTML content saved to: {filename}")
                
                return html_content
            finally:
                driver.quit()
                
        except Exception as e:
            print(f"Selenium failed: {e}")
            print("Trying fallback method with requests...")
            
            # Fallback to simple requests (won't work with JS-rendered content, but for debugging)
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
                }
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                html_content = response.text
                
                # Save fallback HTML content to file for debugging
                filename = f"credly_html_{self.USER}_fallback.html"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(html_content)
                print(f"Fallback HTML content saved to: {filename}")
                print("Note: This may not contain JavaScript-rendered badges")
                
                return html_content
                
            except Exception as fallback_error:
                print(f"Fallback method also failed: {fallback_error}")
                return None

    def sort_by(self):
        """Return sort parameter for Credly URL"""
        return "most_popular" if self.SORT == "POPULAR" else "-state_updated_at"

    def convert_to_dict(self, htmlBadge):
        """Convert badge HTML element to dictionary"""
        soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
        
        # Look for image with different possible class names
        img = None
        possible_img_classes = [
            "settings__skills-profile__edit-skills-profile__badge-card__badge-image",
            "cr-standard-grid-item-content__image",
            "cr-public-earned-badge-grid-item__image",
            "badge-image"
        ]
        
        for img_class in possible_img_classes:
            imgs = soupBadge.findAll("img", {"class": img_class})
            if imgs:
                img = imgs[0]
                break
        
        if not img:
            # Fallback: find any img tag
            img = soupBadge.find("img")
        
        if not img:
            return None
        
        # Get badge title from the new structure
        title = ""
        title_element = soupBadge.find("div", {"class": lambda x: x and "organization-name-two-lines" in x})
        if title_element:
            title = title_element.get_text(strip=True)
        else:
            # Fallback to alt text
            title = img.get("alt", "Badge")
        
        # Get issuer
        issuer = ""
        issuer_element = soupBadge.find("div", {"class": lambda x: x and "issuer-name-two-lines" in x})
        if issuer_element:
            issuer = issuer_element.get_text(strip=True)
        
        # Get issue date
        issue_date = ""
        issue_date_element = soupBadge.find("div", {"class": lambda x: x and "badge-card__issued" in x})
        if issue_date_element:
            date_text = issue_date_element.get_text(strip=True)
            # Extract date from "Emitida dd/mm/yy" format
            import re
            date_match = re.search(r'(\d{2}/\d{2}/\d{2})', date_text)
            if date_match:
                issue_date = date_match.group(1)
        
        # Get image source and adjust size
        img_src = img.get("src", "")
        if img_src:
            # Replace size in URL if it contains size parameters
            if "/size/80x80/" in img_src:
                img_src = img_src.replace("/size/80x80/", f"/size/{self.BADGE_SIZE}x{self.BADGE_SIZE}/")
            elif "110x110" in img_src:
                img_src = img_src.replace("110x110", f"{self.BADGE_SIZE}x{self.BADGE_SIZE}")
            elif "/w_" in img_src:
                # Handle Cloudinary-style URLs
                img_src = img_src.replace("/w_110", f"/w_{self.BADGE_SIZE}")
        
        # For new structure, we need to construct the badge URL from the image URL
        badge_href = ""
        if img_src:
            # Extract badge ID from image URL if possible
            # Example: https://images.credly.com/size/80x80/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png
            try:
                import re
                badge_id_match = re.search(r'/images/([a-f0-9-]+)/', img_src)
                if badge_id_match:
                    badge_id = badge_id_match.group(1)
                    badge_href = f"{self.BASE_URL}/badges/{badge_id}"
            except:
                pass
        
        # Fallback for old structure
        if not badge_href and hasattr(htmlBadge, 'get'):
            badge_href = self.BASE_URL + htmlBadge.get("href", "")
        
        return {
            "title": title.replace('"', '\\"'),
            "href": badge_href,
            "img": img_src,
            "issuer": issuer,
            "issue_date": issue_date
        }

    def return_badges_html(self):
        """Get all badge HTML elements from the page"""
        data = self.data_from_html()
        if not data:
            return []
            
        soup = BeautifulSoup(data, "lxml")
        
        # Look for the new badge structure
        badges = soup.findAll("div", {"class": lambda x: x and "badge-card__card" in x})
        
        if not badges:
            # Fallback to try old structure
            possible_badge_classes = [
                "cr-public-earned-badge-grid-item",
                "cr-earned-badge-grid-item",
                "badge-grid-item"
            ]
            
            for badge_class in possible_badge_classes:
                badges = soup.findAll("a", {"class": badge_class})
                if badges:
                    break
        
        print(f"Found {len(badges)} badge elements in HTML")
        return badges

    def generate_md_format(self, badges):
        """Generate markdown format for badges"""
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
        """Get markdown representation of badges"""
        badges_html = self.return_badges_html()
        
        if self.NUMBER_BADGES > 0:
            badges_html = badges_html[:self.NUMBER_BADGES]
        
        badge_dicts = []
        for badge in badges_html:
            badge_dict = self.convert_to_dict(badge)
            if badge_dict:
                badge_dicts.append(badge_dict)
        
        # Sort badges by issue date (newest first)
        def parse_date(date_str):
            if not date_str:
                return None
            try:
                day, month, year = date_str.split('/')
                # Convert 2-digit year to 4-digit year
                year = '20' + year if int(year) < 50 else '19' + year
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except:
                return None
        
        # Show extracted dates for debugging
        print("\nExtracted badge dates:")
        for badge in badge_dicts:
            print(f"  {badge['title']}: {badge.get('issue_date', 'No date')}")
        
        # Sort by date, putting badges without dates at the end
        badge_dicts.sort(key=lambda x: parse_date(x.get('issue_date', '')) or '1900-01-01', reverse=True)
        
        print("\nSorted badges (newest first):")
        for badge in badge_dicts:
            print(f"  {badge['title']}: {badge.get('issue_date', 'No date')}")
        
        return self.generate_md_format(badge_dicts)

    def save_markdown_to_file(self, filename="badges.md"):
        """Save markdown representation of badges to a file"""
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
    """Main function for testing the Credly scraper"""
    print("Testing Credly scraper...")
    
    # Test with default settings
    credly = Credly()
    
    print(f"Fetching badges for user: {credly.USER}")
    print(f"Sort order: {credly.SORT}")
    print(f"Badge size: {credly.BADGE_SIZE}")
    print(f"Number of badges: {credly.NUMBER_BADGES}")
    
    # Test getting badges HTML
    badges_html = credly.return_badges_html()
    print(f"Found {len(badges_html)} badges")
    
    # Test markdown generation and save to file
    markdown = credly.get_markdown()
    
    if markdown:
        print("\nGenerated markdown (sorted by issue date - newest first):")
        print(markdown)
        
        # Save markdown to file
        credly.save_markdown_to_file("badges.md")
    else:
        print("No markdown generated - check if badges were found")
    
    return markdown


if __name__ == "__main__":
    main()
