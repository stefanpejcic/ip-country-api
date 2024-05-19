

## Build

```bash
docker build -t flask-geoip-app .
```


## Run

```bash
docker run -d -p 80:80 \
    --name flask-geoip-app \
    --restart always \
    --health-cmd="curl -f http://localhost:80/health || exit 1" \
    --health-interval=30s \
    --health-retries=3 \
    --health-timeout=10s \
    --cpus=1 \
    --memory=1g \
    flask-geoip-app
```
