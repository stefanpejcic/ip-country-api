# flask-country-code-for-ip
Simple flask app to just return 2-letter country code for IP address, using MaxMind's GeoLite2 Country database



## Build

```bash
docker build -t flask-geoip-app .
```


## Run

```bash
docker run -d -p 5000:5000 --name flask-geoip-app flask-geoip-app
```
