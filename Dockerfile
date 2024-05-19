# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask geoip2

# Download the latest GeoIP2 database
RUN apt-get update && apt-get install -y wget && \
    wget -O GeoLite2-Country.mmdb https://git.io/GeoLite2-Country.mmdb && \
    apt-get remove -y wget && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the port
EXPOSE 5000

# Entrypoint
CMD ["python", "app.py"]
