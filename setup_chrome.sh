#!/bin/bash

# Docker-specific setup script for Chrome and ChromeDriver
# This script is optimized for container environments

echo "Setting up Chrome and ChromeDriver for Docker environment..."

# Update package list
apt-get update

# Install dependencies
apt-get install -y wget curl unzip gnupg2 software-properties-common

# Install Google Chrome
if ! command -v google-chrome &> /dev/null; then
    echo "Installing Google Chrome..."
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    apt-get update
    apt-get install -y google-chrome-stable
else
    echo "Google Chrome is already installed"
fi

# Verify Chrome installation
CHROME_VERSION=$(google-chrome --version)
echo "Chrome version: $CHROME_VERSION"


# Install webdriver-manager
echo "Installing webdriver-manager..."
pip3 install webdriver-manager

# Clean up to reduce image size
apt-get clean
rm -rf /var/lib/apt/lists/*

echo "Docker setup complete!"
echo "ChromeDriver will be managed by webdriver-manager" 