```console
$ kubectl create deployment todo-dep --image="thepapermen/devopswithkubernetes:todo-0.1.0-slim"
deployment.apps/todo-dep created

$ kubectl get pods
NAME                                 READY   STATUS                   RESTARTS      AGE
hashgenerator-dep-5f67bd4db8-dmrrb   0/1     ContainerStatusUnknown   1 (5d ago)    5d17h
hashgenerator-dep-5f67bd4db8-cbgxh   0/1     ContainerStatusUnknown   1             5d
hashgenerator-dep-5f67bd4db8-flfnp   0/1     Completed                0             5d
logoutput-dep-5fcd68dd9c-9dd2w       1/1     Running                  1 (89m ago)   19h
hashgenerator-dep-5f67bd4db8-pzgmv   1/1     Running                  3 (89m ago)   5d
todo-dep-58f74cfff4-s8ddl            1/1     Running                  0             71s

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
hashgenerator-dep   1/1     1            1           5d17h
logoutput-dep       1/1     1            1           19h
todo-dep            1/1     1            1           107s
```