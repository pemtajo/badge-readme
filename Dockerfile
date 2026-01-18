FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen --no-install-project

# Copy the rest of the code
COPY . .

# Install dependencies and setup Chrome using Docker-specific script
RUN chmod +x setup_chrome.sh
RUN ./setup_chrome.sh

# Test ChromeDriver before running main app
RUN uv run python test_chromedriver.py

RUN ls -la

# Run the application
CMD ["uv", "run", "python", "main.py"]
