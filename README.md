# Simple-docker-flask-app
![image](https://github.com/DiptoChakrabarty/simple-docker-flask-app/blob/main/static/dockerflask.jpeg)

## Steps to run in docker

- [Link for running flask api in docker over here](https://diptochakrabarty.medium.com/build-and-deploy-flask-app-using-docker-13b592830a26)
- [Link for adding swagger to flask api over here](https://diptochakrabarty.medium.com/flask-python-swagger-for-rest-apis-6efdf0100bd7)

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
