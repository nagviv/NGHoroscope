FROM node:18-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/
COPY --from=frontend-build /app/frontend/dist /var/www/html

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD service nginx start && uvicorn app.main:app --host 0.0.0.0 --port 8000
