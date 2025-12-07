FROM python:3.10-slim

RUN apt update \
    && apt install -y wget gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt update \
    && apt install -y google-chrome-stable \
    && pip install selenium webdriver-manager pytest

WORKDIR /app
COPY . .

CMD ["pytest", "-v"]
