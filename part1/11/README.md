```console
$ docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube

$ kubectl apply -f manifests-volumes/ && kubectl apply -f manifests/
persistentvolume/pingpong-pv created
persistentvolumeclaim/pingpong-claim created
deployment.apps/logoutput-dep created
deployment.apps/pingpong-dep created
ingress.networking.k8s.io/pingpong-logoutput-ingress-2 created
service/logoutput-svc created
service/pingpong-svc created

$ kubectl get po
NAME                             READY   STATUS    RESTARTS   AGE
pingpong-dep-775677768-55vxx     1/1     Running   0          67s
logoutput-dep-7f69979cb5-dkltg   1/1     Running   0          67s

$ curl -v 127.0.0.1:8081/pingpong
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET /pingpong HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< App Name: Ping Pong App
< Content-Length: 37
< Content-Type: text/html; charset=utf-8
< Date: Sat, 14 Dec 2024 11:55:02 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host 127.0.0.1 left intact


$ curl -v 127.0.0.1:8081/
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
< App Name: Log Output App
< Content-Length: 128
< Content-Type: text/html; charset=utf-8
< Date: Sat, 14 Dec 2024 11:56:02 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
<html><body>
<h1>2024-12-14 11:56:02.382545: 0b2872a5-6d62-41e3-9314-d38b18f9fe42</h1>
<h2>Ping / Pongs: 57</h2>
</body></html>
* Connection #0 to host 127.0.0.1 left intact

$ curl -s 127.0.0.1:8081/pingpong
<html><body><h1>58</h1></body></html>

$ curl -s 127.0.0.1:8081/
<html><body>
<h1>2024-12-14 11:58:45.200542: 0b2872a5-6d62-41e3-9314-d38b18f9fe42</h1>
<h2>Ping / Pongs: 58</h2>
</body></html>
```