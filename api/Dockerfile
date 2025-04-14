FROM python:3.8-slim-buster

LABEL maintainer="https://github.com/AchilleasKn"

# Set working directory
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY api/ api/

# Expose port for Flask API
EXPOSE 5000

# Run the Flask API
CMD ["python3", "api/api.py"]