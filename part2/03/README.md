```console
$ kubectl apply -f manifests/namespace.yaml 
namespace/dwk-exercise-ns created

$ kubectl apply -f manifests/
deployment.apps/logoutput-dep created
deployment.apps/pingpong-dep created
ingress.networking.k8s.io/pingpong-logoutput-ingress-2 created
namespace/dwk-exercise-ns unchanged
service/logoutput-svc created
service/pingpong-svc created

$ kubens
default
kube-system
kube-public
kube-node-lease
dwk-exercise-ns

$ kubectl get all -n dwk-exercise-ns
NAME                                 READY   STATUS    RESTARTS   AGE
pod/pingpong-dep-85bfc7c7c4-rr9b9    1/1     Running   0          5m22s
pod/logoutput-dep-654fc6d9f5-cx72g   1/1     Running   0          5m22s

NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/logoutput-svc   ClusterIP   10.43.211.31   <none>        2345/TCP   5m22s
service/pingpong-svc    ClusterIP   10.43.207.33   <none>        2346/TCP   5m22s

NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/pingpong-dep    1/1     1            1           5m22s
deployment.apps/logoutput-dep   1/1     1            1           5m22s

NAME                                       DESIRED   CURRENT   READY   AGE
replicaset.apps/pingpong-dep-85bfc7c7c4    1         1         1       5m22s
replicaset.apps/logoutput-dep-654fc6d9f5   1         1         1       5m22s

$ http http://127.0.0.1:8081/pingpong
HTTP/1.1 200 OK
App-Name: Ping Pong App
Content-Length: 12
Content-Type: application/json; charset=utf-8
Date: Fri, 27 Dec 2024 20:32:08 GMT
Server: Python/3.13 aiohttp/3.11.10

{
    "count": 2
}

$ http http://127.0.0.1:8081/
HTTP/1.1 200 OK
App-Name: Log Output App
Content-Length: 127
Content-Type: text/html; charset=utf-8
Date: Fri, 27 Dec 2024 20:32:43 GMT
Server: Python/3.13 aiohttp/3.11.10

<html><body>
<h1>2024-12-27 20:32:43.771976: 1d1221af-23e8-4710-b1d0-148317f4f9d5</h1>
<h2>Ping / Pongs: 3</h2>
</body></html>

```