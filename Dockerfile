FROM python:3.10-slim

# Copy code.
COPY . .
# Install dependencies.
RUN chmod +x /setup_chrome.sh
RUN /setup_chrome.sh


CMD python3 /main.py
