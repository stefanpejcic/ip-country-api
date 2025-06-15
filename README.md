# ip-country-api

Returns 2-letter country code for provided IP address, using MaxMind's GeoLite2 Country database

## Usage

Example usage:

```
# curl http://185.21.214.214:5000/
{
  "country": "RS",
  "ip": "82.117.26.22"
}
```

```
# curl http://185.241.214.214:5000/11.88.55.44
{
  "country": "US",
  "ip": "11.88.55.44"
}
```


## Installation

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
