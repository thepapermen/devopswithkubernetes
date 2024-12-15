The cache is persists if the application is down. For testing purposes
it's life was set to 0.1 minute.

Implementation is here: todo/todo/views.py

```console
$ kubectl apply -f manifests-volumes/ && kubectl apply -f manifests/
persistentvolume/todo-pv created
persistentvolumeclaim/todo-claim created
deployment.apps/todo-dep created
ingress.networking.k8s.io/todo-ingress created
service/todo-svc created

$ curl -s http://127.0.0.1:8081/
<html lang="en">
<body>
    <img src="/media/2024-12-15-18:17:38.jpg">
</body>
</html>

$ curl -I http://127.0.0.1:8081/media/2024-12-15-18:17:38.jpg
HTTP/1.1 200 OK
Content-Disposition: inline; filename="2024-12-15-18:17:38.jpg"
Content-Length: 92500
Content-Type: image/jpeg
Cross-Origin-Opener-Policy: same-origin
Date: Sun, 15 Dec 2024 18:18:40 GMT
Last-Modified: Sun, 15 Dec 2024 18:17:39 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

$ $ curl -v http://127.0.0.1:8081/
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Length: 86
< Content-Type: text/html; charset=utf-8
< Cross-Origin-Opener-Policy: same-origin
< Date: Sun, 15 Dec 2024 18:34:45 GMT
< Referrer-Policy: same-origin
< Server: WSGIServer/0.2 CPython/3.12.4
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< 
<html lang="en">
<body>
    <img src="/media/2024-12-15-18:34:43.jpg">
</body>
* Connection #0 to host 127.0.0.1 left intact
</html>

$ curl -v http://127.0.0.1:8081/
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Length: 86
< Content-Type: text/html; charset=utf-8
< Cross-Origin-Opener-Policy: same-origin
< Date: Sun, 15 Dec 2024 18:34:48 GMT
< Referrer-Policy: same-origin
< Server: WSGIServer/0.2 CPython/3.12.4
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< 
<html lang="en">
<body>
    <img src="/media/2024-12-15-18:34:43.jpg">
</body>
* Connection #0 to host 127.0.0.1 left intact
</html>

$ curl -v http://127.0.0.1:8081/
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Length: 86
< Content-Type: text/html; charset=utf-8
< Cross-Origin-Opener-Policy: same-origin
< Date: Sun, 15 Dec 2024 18:34:50 GMT
< Referrer-Policy: same-origin
< Server: WSGIServer/0.2 CPython/3.12.4
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< 
<html lang="en">
<body>
    <img src="/media/2024-12-15-18:34:50.jpg">
</body>
* Connection #0 to host 127.0.0.1 left intact
</html>

$ curl -I http://127.0.0.1:8081/media/2024-12-15-18:34:50.jpg
HTTP/1.1 200 OK
Content-Disposition: inline; filename="2024-12-15-18:34:50.jpg"
Content-Length: 341798
Content-Type: image/jpeg
Cross-Origin-Opener-Policy: same-origin
Date: Sun, 15 Dec 2024 18:42:58 GMT
Last-Modified: Sun, 15 Dec 2024 18:34:50 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

$ kubectl get po
NAME                        READY   STATUS    RESTARTS   AGE
todo-dep-696fc8f846-9tn2s   1/1     Running   0          30m

$ kubectl delete pod todo-dep-696fc8f846-9tn2s
pod "todo-dep-696fc8f846-9tn2s" deleted

$ kubectl get po
NAME                        READY   STATUS    RESTARTS   AGE
todo-dep-696fc8f846-zwh49   1/1     Running   0          15s

$ curl -I http://127.0.0.1:8081/media/2024-12-15-18:34:50.jpg
HTTP/1.1 200 OK
Content-Disposition: inline; filename="2024-12-15-18:34:50.jpg"
Content-Length: 341798
Content-Type: image/jpeg
Cross-Origin-Opener-Policy: same-origin
Date: Sun, 15 Dec 2024 18:44:26 GMT
Last-Modified: Sun, 15 Dec 2024 18:34:50 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

$ docker exec k3d-k3s-default-agent-0 ls /tmp/kube
2024-12-15-18:34:50.jpg
pingpong.txt

$ kubectl delete -f manifests/ && kubectl delete -f manifests-volumes
deployment.apps "todo-dep" deleted
ingress.networking.k8s.io "todo-ingress" deleted
service "todo-svc" deleted
persistentvolume "todo-pv" deleted
persistentvolumeclaim "todo-claim" deleted

$ docker exec k3d-k3s-default-agent-0 ls /tmp/kube
2024-12-15-18:34:50.jpg
pingpong.txt
```