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

```