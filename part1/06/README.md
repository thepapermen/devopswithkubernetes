```console
$ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-dep created

$ kubectl get po
NAME                       READY   STATUS    RESTARTS   AGE
todo-dep-678969c9c-qpl66   1/1     Running   0          2m7s

$ kubectl apply -f manifests/service.yaml
The Service "todo-svc" is invalid: spec.ports[0].nodePort: Invalid value: 30080: provided port is already allocated

$ kubectl get services
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes         ClusterIP   10.43.0.1      <none>        443/TCP          26m
hashresponse-svc   NodePort    10.43.49.113   <none>        1234:30080/TCP   11m

$ kubectl delete service hashresponse-svc
service "hashresponse-svc" deleted

$ kubectl apply -f manifests/service.yaml
service/todo-svc created

$ http GET 127.0.0.1:8082
HTTP/1.1 200 OK
Content-Length: 12068
Content-Type: text/html; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 11 Dec 2024 17:48:32 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.4
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

<!doctype html>

<html lang="en-us" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>The install worked successfully! Congratulations!</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    [...]
    
    [Console output of HTTPie truncated for brevity]

```