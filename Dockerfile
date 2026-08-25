# Stage 1: Build React Frontend
FROM node:18-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python Backend & Nginx Runtime
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies and Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application
COPY app/ ./app/
COPY tests/ ./tests/

# Copy built frontend assets to Nginx public folder
COPY --from=frontend-build /app/frontend/dist /var/www/html

# Configure Nginx
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# Start Nginx and FastAPI via shell
CMD service nginx start && uvicorn app.main:app --host 0.0.0.0 --port 8000
