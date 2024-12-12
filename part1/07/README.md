```console
$ kubectl apply -f manifests/
deployment.apps/logoutput-dep created
ingress.networking.k8s.io/logoutput-ingress created
service/logoutput-svc created

$ kubectl get svc,ing
NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes      ClusterIP   10.43.0.1      <none>        443/TCP    132m
service/logoutput-svc   ClusterIP   10.43.189.77   <none>        2345/TCP   2s

NAME                                          CLASS    HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/logoutput-ingress   <none>   *       172.18.0.2,172.18.0.4,172.18.0.5   80      2s

$ curl -v http://localhost:8081/
*   Trying ::1:8081...
* TCP_NODELAY set
* Connected to localhost (::1) port 8081 (#0)
> GET / HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< App Name: Log Output App
< Content-Length: 99
< Content-Type: text/html; charset=utf-8
< Date: Thu, 12 Dec 2024 12:23:57 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host localhost left intact
<html><body><h1>2024-12-12 12:23:57.175332: 60a4c2b3-7153-4549-a7e1-32e26aa948c9</h1></body></html>
```