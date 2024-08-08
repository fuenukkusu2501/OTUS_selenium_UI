# Устанавка базового образ
FROM python:3.12-alpine

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# # Копирование cm_linux_amd64 в контейнер
# COPY cm_linux_amd64 /app/cm_linux_amd64
#
# # Предоставление прав на выполнение
# RUN chmod +x /app/cm_linux_amd64
#
# # Запуск контейнеров selenoid
# RUN ./app/cm_linux_amd64 selenoid start
# RUN ./app/cm_linux_amd64 selenoid-ui start

# Запуск тестов
ENTRYPOINT ["pytest"]