```console
$ kubectl apply -f manifests/
deployment.apps/todo-dep configured
ingress.networking.k8s.io/todo-ingress created
service/todo-svc created

$ kubectl get svc,ing,po
NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.43.0.1      <none>        443/TCP    149m
service/todo-svc     ClusterIP   10.43.67.206   <none>        2345/TCP   70s

NAME                                     CLASS    HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/todo-ingress   <none>   *       172.18.0.2,172.18.0.4,172.18.0.5   80      70s

NAME                            READY   STATUS    RESTARTS   AGE
pod/todo-dep-57d9ff864b-6jsrk   1/1     Running   0          70s


$ http GET http://localhost:8081/
HTTP/1.1 200 OK
Content-Length: 12068
Content-Type: text/html; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 11 Dec 2024 19:52:24 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

<!doctype html>

<html lang="en-us" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>The install worked successfully! Congratulations!</title>

    [...]
    
    [Console output of HTTPie truncated for brevity]

```