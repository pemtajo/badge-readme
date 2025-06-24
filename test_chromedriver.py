#!/usr/bin/env python3
"""
Test script to verify ChromeDriver setup is working correctly
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_chromedriver():
    """Test ChromeDriver initialization"""
    print("Testing ChromeDriver setup...")
    
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Try webdriver-manager first
        print("Attempting to use webdriver-manager...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Test basic functionality
        print("ChromeDriver initialized successfully!")
        driver.get("https://www.google.com")
        title = driver.title
        print(f"Successfully loaded Google, page title: {title}")
        
        driver.quit()
        print("✅ ChromeDriver test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ ChromeDriver test FAILED: {e}")
        return False

if __name__ == "__main__":
    success = test_chromedriver()
    exit(0 if success else 1) 