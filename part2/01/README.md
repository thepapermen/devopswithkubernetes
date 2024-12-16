```console
$ kubectl apply -f manifests/
deployment.apps/logoutput-dep created
deployment.apps/pingpong-dep created
ingress.networking.k8s.io/pingpong-logoutput-ingress-2 created
service/logoutput-svc created
service/pingpong-svc created

$ curl -s http://127.0.0.1:8081/pingpong
{"count": 1}

$ curl -s http://127.0.0.1:8081/
<html><body>
<h1>2024-12-16 12:33:52.379672: 17499ee1-6f35-4913-99b3-654092617d0f</h1>
<h2>Ping / Pongs: 2</h2>
</body></html>

```