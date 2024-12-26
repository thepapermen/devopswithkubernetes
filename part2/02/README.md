The result of this exercise is one service more complicated than the requirement,
hopefully my solution will be accepted nevertheless: The logic to serve and store random pictures is
not on frontend, but in a separate service.

Reasoning:
Since Django is just too much to serve html and js, Django-based todo is refactored to become
Todo Backend. TypeScript-based todo Frontend is created, comprised of only static files is made to run on a lightweight
busybox image with httpd. To fulfil the requirement to not serve image from Todo Backend,
Image Cache is refactored out of Django App and moved to a separate Image Cache Backend. 
To compare with the previous state of Todo App, check the folder part1/13. 

Theoretically, the requirement to fetch images from Frontend can be solved by making the
Frontend docker container serve both static files and run the image-backend/serve_image.py script
as well, I just think in my case it will be a bit uglier solution, but still can be implemented without
significant changes to the underlying code.

Production config for frontend is stored in the todo-frontend/env.production

```console
$ kubectl apply -f manifests-volumes/ && kubectl apply -f manifests/
persistentvolume/image-pv created
persistentvolumeclaim/image-claim created
deployment.apps/todo-image-backend-dep created
deployment.apps/todo-backend-dep created
deployment.apps/todo-frontend-dep created
ingress.networking.k8s.io/todo-ingress created
service/todo-image-backend-svc created
service/todo-backend-svc created
service/todo-frontend-svc created

$ kubectl get -f manifests/
NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-image-backend-dep   1/1     1            1           4m41s
deployment.apps/todo-backend-dep         1/1     1            1           4m41s
deployment.apps/todo-frontend-dep        1/1     1            1           4m41s

NAME                                     CLASS    HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/todo-ingress   <none>   *       172.18.0.2,172.18.0.3,172.18.0.4   80      4m41s

NAME                             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/todo-image-backend-svc   ClusterIP   10.43.112.64    <none>        2345/TCP   4m41s
service/todo-backend-svc         ClusterIP   10.43.136.172   <none>        2346/TCP   4m40s
service/todo-frontend-svc        ClusterIP   10.43.227.45    <none>        2347/TCP   4m40s


$ http GET http://127.0.0.1:8081/image
HTTP/1.1 200 OK
App-Name: Image Backend App
Content-Length: 117917
Content-Type: image/jpeg
Date: Thu, 26 Dec 2024 17:40:42 GMT
Server: Python/3.13 aiohttp/3.11.11



+-----------------------------------------+
| NOTE: binary data not shown in terminal |
+-----------------------------------------+

$ http GET http://127.0.0.1:8081/api/
HTTP/1.1 200 OK
Content-Length: 579
Content-Type: application/json; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 26 Dec 2024 17:41:24 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.8
Vary: origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "count": 8,
    "items": [
        {
            "created_at": "2024-12-21T20:35:28.544Z",
            "id": 1,
            "txt": "ahoj"
        },
    # ... OUTPUT TRUNCATED FOR BREVITY ...
        {
            "created_at": "2024-12-26T17:26:00.334Z",
            "id": 8,
            "txt": "new todo"
        }
    ]
}

$ http POST http://127.0.0.1:8081/api/ txt='kubetodo'
HTTP/1.1 201 Created
Content-Length: 70
Content-Type: application/json; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 26 Dec 2024 17:44:37 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.8
Vary: origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "created_at": "2024-12-26T17:44:37.508Z",
    "id": 9,
    "txt": "kubetodo"
}

$ http GET http://127.0.0.1:8081/
HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 428
Content-Type: text/html
Date: Thu, 26 Dec 2024 17:46:19 GMT
Etag: "676d8ea6-1ac"
Last-Modified: Thu, 26 Dec 2024 17:13:10 GMT

<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
    <script type="module" crossorigin src="/assets/index-BHu9Wa4D.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-DgK3D5EH.css">
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>

```

![Frontend](https://github.com/thepapermen/devopswithkubernetes/blob/main/part2/02/Screenshot-from-2024-12-26-18-48-40.png?raw=true Frontend)