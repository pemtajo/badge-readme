FROM python
# Copy code.
COPY . .
# Install dependencies.
RUN chmod +x /setup_chrome.sh
RUN /setup_chrome.sh


CMD python3 /main.py
