FROM python:3.14.2-slim-trixie

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the rest of the code
COPY . .

# Install dependencies and setup Chrome using Docker-specific script
RUN chmod +x setup_chrome.sh
RUN ./setup_chrome.sh

# Test ChromeDriver before running main app
RUN python3 test_chromedriver.py

RUN ls -la

# Run the application
CMD ["python3", "/app/main.py"]
