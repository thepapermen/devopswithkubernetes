```console
$ kubectl apply -f manifests/namespace.yaml \
&& kubectl apply -f manifests/ \
&& kubectl apply -f manifests-volumes/

namespace/dwk-todo-project-ns created
deployment.apps/todo-image-backend-dep created
deployment.apps/todo-backend-dep created
deployment.apps/todo-frontend-dep created
ingress.networking.k8s.io/todo-ingress created
namespace/dwk-todo-project-ns unchanged
service/todo-image-backend-svc created
service/todo-backend-svc created
service/todo-frontend-svc created
persistentvolume/image-pv created
persistentvolumeclaim/image-claim created

$ kubens
default
kube-system
kube-public
kube-node-lease
dwk-todo-project-ns

$ kubens dwk-todo-project-ns
Context "k3d-k3s-default" modified.
Active namespace is "dwk-todo-project-ns".

$ kubectl get po
NAME                                      READY   STATUS    RESTARTS   AGE
todo-frontend-dep-57c455c4f7-lkn7d        1/1     Running   0          7m21s
todo-backend-dep-59d656b484-4tjlv         1/1     Running   0          7m21s
todo-image-backend-dep-5bc66b64fb-z9mxf   1/1     Running   0          7m21s


$ http GET http://127.0.0.1:8081/image
HTTP/1.1 200 OK
App-Name: Image Backend App
Content-Length: 141694
Content-Type: image/jpeg
Date: Fri, 27 Dec 2024 21:13:19 GMT
Server: Python/3.13 aiohttp/3.11.11



+-----------------------------------------+
| NOTE: binary data not shown in terminal |
+-----------------------------------------+

$ http POST http://127.0.0.1:8081/api/ txt='newkubetodo' 
HTTP/1.1 201 Created
Content-Length: 73
Content-Type: application/json; charset=utf-8
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 27 Dec 2024 21:15:26 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.8
Vary: origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "created_at": "2024-12-27T21:15:26.037Z",
    "id": 11,
    "txt": "newkubetodo"
}


$ http GET http://127.0.0.1:8081/
HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 428
Content-Type: text/html
Date: Fri, 27 Dec 2024 21:16:53 GMT
Etag: "676d8ea6-1ac"
Last-Modified: Thu, 26 Dec 2024 17:13:10 GMT

<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
    <script type="module" crossorigin src="/assets/index-BHu9Wa4D.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-DgK3D5EH.css">
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>

$ kubectl get all --all-namespaces
NAMESPACE             NAME                                          READY   STATUS      RESTARTS        AGE
kube-system           pod/helm-install-traefik-crd--1-6pggq         0/1     Completed   0               16d
kube-system           pod/helm-install-traefik--1-tjgx6             0/1     Completed   2               16d
kube-system           pod/coredns-96cc4f57d-ntfc4                   1/1     Running     26 (102m ago)   16d
kube-system           pod/local-path-provisioner-84bb864455-w4d5t   1/1     Running     33 (102m ago)   16d
kube-system           pod/svclb-traefik-rhmjt                       2/2     Running     48 (102m ago)   16d
kube-system           pod/svclb-traefik-blgvl                       2/2     Running     48 (101m ago)   16d
kube-system           pod/metrics-server-ff9dbcb6c-t8552            1/1     Running     31 (101m ago)   16d
kube-system           pod/traefik-56c4b88c4b-bgxjg                  1/1     Running     28 (101m ago)   16d
kube-system           pod/svclb-traefik-qtnpn                       2/2     Running     48 (101m ago)   16d
dwk-todo-project-ns   pod/todo-frontend-dep-57c455c4f7-lkn7d        1/1     Running     0               12m
dwk-todo-project-ns   pod/todo-backend-dep-59d656b484-4tjlv         1/1     Running     0               12m
dwk-todo-project-ns   pod/todo-image-backend-dep-5bc66b64fb-z9mxf   1/1     Running     0               12m

NAMESPACE             NAME                             TYPE           CLUSTER-IP      EXTERNAL-IP                        PORT(S)                      AGE
default               service/kubernetes               ClusterIP      10.43.0.1       <none>                             443/TCP                      16d
kube-system           service/kube-dns                 ClusterIP      10.43.0.10      <none>                             53/UDP,53/TCP,9153/TCP       16d
kube-system           service/metrics-server           ClusterIP      10.43.121.58    <none>                             443/TCP                      16d
kube-system           service/traefik                  LoadBalancer   10.43.189.80    172.18.0.2,172.18.0.3,172.18.0.5   80:31117/TCP,443:30320/TCP   16d
dwk-todo-project-ns   service/todo-image-backend-svc   ClusterIP      10.43.97.152    <none>                             2345/TCP                     12m
dwk-todo-project-ns   service/todo-backend-svc         ClusterIP      10.43.209.171   <none>                             2346/TCP                     12m
dwk-todo-project-ns   service/todo-frontend-svc        ClusterIP      10.43.169.101   <none>                             2347/TCP                     12m

NAMESPACE     NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
kube-system   daemonset.apps/svclb-traefik   3         3         3       3            3           <none>          16d

NAMESPACE             NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
kube-system           deployment.apps/coredns                  1/1     1            1           16d
kube-system           deployment.apps/local-path-provisioner   1/1     1            1           16d
kube-system           deployment.apps/metrics-server           1/1     1            1           16d
kube-system           deployment.apps/traefik                  1/1     1            1           16d
dwk-todo-project-ns   deployment.apps/todo-frontend-dep        1/1     1            1           12m
dwk-todo-project-ns   deployment.apps/todo-backend-dep         1/1     1            1           12m
dwk-todo-project-ns   deployment.apps/todo-image-backend-dep   1/1     1            1           12m

NAMESPACE             NAME                                                DESIRED   CURRENT   READY   AGE
kube-system           replicaset.apps/coredns-96cc4f57d                   1         1         1       16d
kube-system           replicaset.apps/local-path-provisioner-84bb864455   1         1         1       16d
kube-system           replicaset.apps/metrics-server-ff9dbcb6c            1         1         1       16d
kube-system           replicaset.apps/traefik-56c4b88c4b                  1         1         1       16d
dwk-todo-project-ns   replicaset.apps/todo-frontend-dep-57c455c4f7        1         1         1       12m
dwk-todo-project-ns   replicaset.apps/todo-backend-dep-59d656b484         1         1         1       12m
dwk-todo-project-ns   replicaset.apps/todo-image-backend-dep-5bc66b64fb   1         1         1       12m

NAMESPACE     NAME                                 COMPLETIONS   DURATION   AGE
kube-system   job.batch/helm-install-traefik-crd   1/1           96s        16d
kube-system   job.batch/helm-install-traefik       1/1           111s       16d

```
See Screenshot of the frontend in part2/02