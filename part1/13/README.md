```console
$ kubectl apply -f manifests-volumes/ && kubectl apply -f manifests/
persistentvolume/todo-pv created
persistentvolumeclaim/todo-claim created
deployment.apps/todo-dep created
ingress.networking.k8s.io/todo-ingress created
service/todo-svc created

$ curl -s http://127.0.0.1:8081/
<html lang="en">
<body style="text-align: center;">
    <img src="/media/2024-12-15-19:06:44.jpg" width="300">

    <form><input name="todo" maxlength="140"><button>Create TODO</button></form>
    <ul>
        <li>TODO 1</li>
        <li>TODO 2</li>
    </ul>
</body>
</html>
```