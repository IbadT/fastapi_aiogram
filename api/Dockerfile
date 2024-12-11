# Используем официальный образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
# COPY ../requirements.txt .
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код FastAPI
# COPY . .
COPY ./api /app

# Устанавливаем переменные окружения
# ENV PYTHONUNBUFFERED=1

# Команда для запуска FastAPI сервера
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
