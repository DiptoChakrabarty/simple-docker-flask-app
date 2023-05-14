# Simple-docker-flask-app

## Steps to run in docker

- [Link over here](https://diptochakrabarty.medium.com/build-and-deploy-flask-app-using-docker-13b592830a26)

## Steps to run using python

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