FROM python:3.11-slim

WORKDIR /app

# Install curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 8000

# Healthcheck
# You can use this in terminal
  CMD curl -f http://localhost:8000/healthcheck \
   && curl -f http://localhost:8000/books \
   || exit 1

# Command to run the app
CMD ["uvicorn", "book_api.app.main:app", "--host", "0.0.0.0", "--port", "8000"]