FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ ./app

WORKDIR /app/app

# Run Flask via gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

