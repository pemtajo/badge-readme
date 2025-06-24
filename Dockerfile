FROM python:3.10-slim

# Install dependencies.
RUN chmod +x /setup_chrome.sh
RUN /setup_chrome.sh

# Copy code.
COPY . .

CMD python3 /main.py
