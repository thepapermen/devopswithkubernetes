```console
$ kubectl apply -f manifests/
deployment.apps/logoutput-dep created
ingress.networking.k8s.io/logoutput-ingress created
service/logoutput-svc created

$ kubectl get svc,ing,po
NAME                    TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
service/kubernetes      ClusterIP   10.43.0.1    <none>        443/TCP    26h
service/logoutput-svc   ClusterIP   10.43.3.32   <none>        2345/TCP   49s

NAME                                          CLASS    HOSTS   ADDRESS                            PORTS   AGE
ingress.networking.k8s.io/logoutput-ingress   <none>   *       172.18.0.2,172.18.0.4,172.18.0.5   80      49s

NAME                                 READY   STATUS    RESTARTS   AGE
pod/logoutput-dep-8675897d4c-mh2c2   2/2     Running   0          49s

$ kubectl describe pod/logoutput-dep-8675897d4c-mh2c2
Name:             logoutput-dep-8675897d4c-mh2c2
Namespace:        default
Priority:         0
Service Account:  default
Node:             k3d-k3s-default-agent-0/172.18.0.4
Start Time:       Thu, 12 Dec 2024 21:10:23 +0100
Labels:           app=logoutput
                  pod-template-hash=8675897d4c
Annotations:      <none>
Status:           Running
IP:               10.42.2.22
IPs:
  IP:           10.42.2.22
Controlled By:  ReplicaSet/logoutput-dep-8675897d4c
Containers:
  showoutput:
    Container ID:   containerd://61af5ee3468812c99b0a3ac007b456ac45b377f7e0e5cf850bd0ba98e6472bf7
    Image:          thepapermen/devopswithkubernetes:showoutput-0.3.0-alpine
    Image ID:       docker.io/thepapermen/devopswithkubernetes@sha256:c806df207540f0a21cd8ed6cc153250e4c860adaf2bee16876f0257acebc89c3
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Thu, 12 Dec 2024 21:10:24 +0100
    Ready:          True
    Restart Count:  0
    Environment:
      HOST:       0.0.0.0
      PORT:       3000
      FILE_PATH:  /usr/src/app/files/output.txt
    Mounts:
      /usr/src/app/files from shared-logoutput (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7tpxz (ro)
  logoutput:
    Container ID:   containerd://f2058fb608ec8560c1ee2b4b5294dc7af1115d360c2c304ac7cfb28d7bd72914
    Image:          thepapermen/devopswithkubernetes:log_output-0.3.0-alpine
    Image ID:       docker.io/thepapermen/devopswithkubernetes@sha256:48743c513bac8f84e6a372c9e7d2790aa1b67d60f74a8b0729edcdbeb9802a91
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Thu, 12 Dec 2024 21:10:24 +0100
    Ready:          True
    Restart Count:  0
    Environment:
      FILE_PATH:  /usr/src/app/files/output.txt
    Mounts:
      /usr/src/app/files from shared-logoutput (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7tpxz (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  shared-logoutput:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     
    SizeLimit:  <unset>
  kube-api-access-7tpxz:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  90s   default-scheduler  Successfully assigned default/logoutput-dep-8675897d4c-mh2c2 to k3d-k3s-default-agent-0
  Normal  Pulled     90s   kubelet            Container image "thepapermen/devopswithkubernetes:showoutput-0.3.0-alpine" already present on machine
  Normal  Created    90s   kubelet            Created container showoutput
  Normal  Started    89s   kubelet            Started container showoutput
  Normal  Pulled     89s   kubelet            Container image "thepapermen/devopswithkubernetes:log_output-0.3.0-alpine" already present on machine
  Normal  Created    89s   kubelet            Created container logoutput
  Normal  Started    89s   kubelet            Started container logoutput

$ curl -v 127.0.0.1:8081
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< App Name: Show Output App
< Content-Length: 99
< Content-Type: text/html; charset=utf-8
< Date: Thu, 12 Dec 2024 20:12:47 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host 127.0.0.1 left intact
<html><body><h1>2024-12-12 20:12:45.928486: e7c2d26a-de26-417c-b499-7fb0ef8147fc</h1></body></html>

$ curl -v 127.0.0.1:8081
*   Trying 127.0.0.1:8081...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8081 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< App Name: Show Output App
< Content-Length: 99
< Content-Type: text/html; charset=utf-8
< Date: Thu, 12 Dec 2024 20:13:06 GMT
< Server: Python/3.13 aiohttp/3.11.10
< 
* Connection #0 to host 127.0.0.1 left intact
<html><body><h1>2024-12-12 20:13:06.496009: e7c2d26a-de26-417c-b499-7fb0ef8147fc</h1></body></html>

```