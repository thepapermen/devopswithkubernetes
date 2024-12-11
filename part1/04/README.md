```console
$ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-dep created

$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
logoutput-dep-7c47874f85-ttr4m   1/1     Running   0          31m
todo-dep-776b5bb796-d6kxc        1/1     Running   0          109s

$ kubectl get deployments
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
logoutput-dep   1/1     1            1           31m
todo-dep        1/1     1            1           2m21s
```