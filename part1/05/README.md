```console
$ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-dep created

$ kubectl get po
NAME                                 READY   STATUS    RESTARTS   AGE
hashgenerator-dep-548d4d6c8d-k4t6q   1/1     Running   0          29m
hashresponse-dep-869df48685-bc976    1/1     Running   0          26m
todo-dep-678969c9c-5cgk7             1/1     Running   0          2m13s

$ kubectl port-forward todo-dep-678969c9c-5cgk7 3006:3005
Forwarding from 127.0.0.1:3006 -> 3005
Forwarding from [::1]:3006 -> 3005
Handling connection for 3006

$ http GET http://127.0.0.1:3006
HTTP/1.1 200 OK
Content-Length: 12068
Content-Type: text/html; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 11 Dec 2024 17:07:38 GMT
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