FROM python:3.7-slim-buster

# Create directories
RUN mkdir -pv /home/project/flask_app \
    && mkdir -pv /var/ttn_tracker/ssl_certs

# Set working directory
WORKDIR /home/project/flask_app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and SQLite
RUN apt-get update && apt-get install -y build-essential sqlite3

# Copy requirements and install dependencies
COPY requirements.txt /home/project/flask_app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /home/project/flask_app/

# Run SSL certificate generation script
RUN /bin/bash /home/project/flask_app/ssl-certs-generate.sh
