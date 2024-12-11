```console
$ kubectl delete deployment logoutput-dep
deployment.apps "logoutput-dep" deleted

$ kubectl apply -f log_output/manifests/deployment.yaml
deployment.apps/logoutput-dep created

$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
logoutput-dep-7c47874f85-ttr4m   1/1     Running   0          47s

$ kubectl get deployments
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
logoutput-dep   1/1     1            1           110s

$ kubectl logs -f logoutput-dep-7c47874f85-ttr4m
2024-12-10 12:00:42.483221: ec1d04fd-1d9f-422b-ade5-94c8bcf29bc8
2024-12-10 12:00:47.488440: ec1d04fd-1d9f-422b-ade5-94c8bcf29bc8
2024-12-10 12:00:52.491501: ec1d04fd-1d9f-422b-ade5-94c8bcf29bc8
2024-12-10 12:00:57.495471: ec1d04fd-1d9f-422b-ade5-94c8bcf29bc8
2024-12-10 12:01:02.499531: ec1d04fd-1d9f-422b-ade5-94c8bcf29bc8
```