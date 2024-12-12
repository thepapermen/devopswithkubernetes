```console
$ kubectl get svc,ing,po
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.43.0.1    <none>        443/TCP   16h

$ kubectl apply -f ../07/manifests/deployment.yaml 
deployment.apps/logoutput-dep created

$ kubectl apply -f ../07/manifests/service.yaml 
service/logoutput-svc created

$ kubectl apply -f manifests/
deployment.apps/pingpong-dep created
ingress.networking.k8s.io/pingpong-logoutput-ingress created
service/pingpong-svc created

$ kubectl get svc,ing,po
NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes      ClusterIP   10.43.0.1      <none>        443/TCP    19h
service/logoutput-svc   ClusterIP   10.43.95.234   <none>        2345/TCP   3h8m
service/pingpong-svc    ClusterIP   10.43.6.177    <none>        2346/TCP   3h7m

NAME                                                   CLASS    HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/pingpong-logoutput-ingress   <none>   *       172.18.0.2,172.18.0.4,172.18.0.5   80      3h7m

NAME                                 READY   STATUS    RESTARTS   AGE
pod/logoutput-dep-7b5cdcdf76-ph429   1/1     Running   0          79m
pod/pingpong-dep-89754d56d-rpxx9     1/1     Running   0          2m34s

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
< Date: Thu, 12 Dec 2024 13:01:56 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host localhost left intact
<html><body><h1>2024-12-12 13:01:56.360181: 60a4c2b3-7153-4549-a7e1-32e26aa948c9</h1></body></html>  

$ curl -v http://localhost:8081/pingpong
*   Trying ::1:8081...
* TCP_NODELAY set
* Connected to localhost (::1) port 8081 (#0)
> GET /pingpong HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< App Name: Ping Pong App
< Content-Length: 37
< Content-Type: text/html; charset=utf-8
< Date: Thu, 12 Dec 2024 13:04:32 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host localhost left intact
<html><body><h1>11</h1></body></html>
```