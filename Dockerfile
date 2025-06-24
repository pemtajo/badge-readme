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
WORKDIR /app

COPY main.py main.py
COPY . .


# Install Python dependencies globally
RUN pip3 install --upgrade pip
RUN pip3 install webdriver-manager

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create entrypoint script
RUN echo '#!/bin/bash\n\
echo "Setting up environment..."\n\
if [ -f "requirements.txt" ]; then\n\
    echo "Installing Python dependencies from requirements.txt..."\n\
    pip3 install -r requirements.txt\n\
fi\n\
if [ -f "setup_chrome.sh" ]; then\n\
    echo "Running setup script..."\n\
    chmod +x setup_chrome.sh\n\
    ./setup_chrome.sh\n\
fi\n\
if [ -f "test_chromedriver.py" ]; then\n\
    echo "Testing ChromeDriver..."\n\
    python3 test_chromedriver.py\n\
fi\n\
echo "Running main application..."\n\
python3 main.py' > /entrypoint.sh && chmod +x /entrypoint.sh

RUN ls -la

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
