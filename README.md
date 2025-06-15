# ip-country-api

Returns 2-letter country code for provided IP address, using MaxMind's GeoLite2 Country database

Usage:

docker compose:
```
services:
  ip-country-api:
    image: openpanel/ip-country-api
    container_name: ip-country-api
    ports:
      - "5000:5000"
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.1'
          memory: 1G
```

docker run:
```
docker run -d -p 5000:5000 \
    --name ip-country-api \
    --restart always \
    --health-cmd="curl -f http://localhost:5000/health || exit 1" \
    --health-interval=30s \
    --health-retries=3 \
    --health-timeout=10s \
    --cpus=0.1 \
    --memory=0.1g \
    openpanel/ip-country-api
```
