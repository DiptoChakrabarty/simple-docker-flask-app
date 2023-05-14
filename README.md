# Simple-docker-flask-app

## Steps to run

- Setup virtual env
- RUN pip3 install -r requirements.txt
- RUN python3 app.py

## Curl Requests

- Get Request
```
curl http://localhost:8080/
```

- POST Request
```
curl -X POST -H "Content-Type: application/json" \  
    -d '{"name": "ezio", "server": "dchost"}' \
    http://localhost:8080/access
```