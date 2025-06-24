FROM python:3.11-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Set working directory for GitHub Actions
WORKDIR /github/workspace

# Copy code to the working directory
COPY . .

# Install dependencies and setup Chrome using Docker-specific script
RUN chmod +x setup_chrome.sh
RUN ./setup_chrome.sh

# Test ChromeDriver before running main app
RUN python3 test_chromedriver.py

# Run the application
CMD ["python3", "main.py"]
