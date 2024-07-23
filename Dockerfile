# Используем базовый образ Python
FROM python:3.12-alpine

# Устанавливаем зависимости для chromedriver
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont \
    bash \
    libc6-compat

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменные окружения для Selenium
ENV PATH="/usr/bin/:/usr/bin/chromedriver:$PATH"
ENV CHROME_BIN="/usr/bin/google-chrome"
ENV CHROME_DRIVER="/usr/bin/chromedriver"

# Запускаем контейнер
CMD ["pytest"]
