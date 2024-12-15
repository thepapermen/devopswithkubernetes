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

$ curl -sI 127.0.0.1:8081 |grep App
App Name: Log Output App

$ curl -sI 127.0.0.1:8081/pingpong |grep App
App Name: Ping Pong App

$ curl -s 127.0.0.1:8081
<html><body>
<h1>2024-12-14 12:14:55.735906: 0b2872a5-6d62-41e3-9314-d38b18f9fe42</h1>
<h2>Ping / Pongs: 59</h2>
</body></html>

$ curl -s 127.0.0.1:8081/pingpong
<html><body><h1>60</h1></body></html>

$ curl -s 127.0.0.1:8081/pingpong
<html><body><h1>61</h1></body></html>

$ curl -s 127.0.0.1:8081
<html><body>
<h1>2024-12-14 12:16:46.696421: 0b2872a5-6d62-41e3-9314-d38b18f9fe42</h1>
<h2>Ping / Pongs: 61</h2>
</body></html>

```