# Make it run with Docker :

```
$ docker build -t python-api .
$ docker run -it --rm --name python-api -p 5000:5000 python-api

$ curl http://127.0.0.1:5000/
$ curl http://127.0.0.1:5000/api/v1/books
```

