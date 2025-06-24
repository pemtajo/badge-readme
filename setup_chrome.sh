#!/bin/bash

# Setup script for Chrome and ChromeDriver on Linux systems
# This script installs the necessary dependencies for the Credly scraper

echo "Setting up Chrome and ChromeDriver for Credly scraper..."

# Update package list
sudo apt-get update

# Install dependencies
sudo apt-get install -y wget curl unzip

# Install Google Chrome
if ! command -v google-chrome &> /dev/null; then
    echo "Installing Google Chrome..."
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    sudo apt-get update
    sudo apt-get install -y google-chrome-stable
else
    echo "Google Chrome is already installed"
fi

# Install ChromeDriver
if ! command -v chromedriver &> /dev/null; then
    echo "Installing ChromeDriver..."
    # Get the Chrome version
    CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d'.' -f1)
    echo "Chrome version: $CHROME_VERSION"
    
    # Download and install ChromeDriver
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}")
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
    sudo unzip /tmp/chromedriver.zip -d /usr/local/bin/
    sudo chmod +x /usr/local/bin/chromedriver
    rm /tmp/chromedriver.zip
else
    echo "ChromeDriver is already installed"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Setup complete!"
echo "You can now test the scraper with: python3 main.py" 