FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
RUN mkdir -p /app/uploads

# Runs only when we do docker run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]