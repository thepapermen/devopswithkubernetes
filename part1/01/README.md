```console
$ kubectl create deployment logoutput-dep --image="thepapermen/devopswithkubernetes:log_output"
deployment.apps/logoutput-dep created

$ kubectl get pods
NAME                                 READY   STATUS                   RESTARTS        AGE
hashgenerator-dep-5f67bd4db8-dmrrb   0/1     ContainerStatusUnknown   1 (4d4h ago)    4d21h
hashgenerator-dep-5f67bd4db8-cbgxh   0/1     ContainerStatusUnknown   1               4d4h
hashgenerator-dep-5f67bd4db8-flfnp   0/1     Completed                0               4d4h
hashgenerator-dep-5f67bd4db8-pzgmv   1/1     Running                  2 (5h29m ago)   4d4h
logoutput-dep-5fcd68dd9c-9dd2w       1/1     Running                  0               55s

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
hashgenerator-dep   1/1     1            1           4d21h
logoutput-dep       1/1     1            1           79s

$ kubectl logs -f logoutput-dep-5fcd68dd9c-9dd2w
2024-12-09 15:23:49.305408: c11edd65-a835-4c96-83bf-ac0adcb0c986
2024-12-09 15:23:54.310630: c11edd65-a835-4c96-83bf-ac0adcb0c986
2024-12-09 15:23:59.314567: c11edd65-a835-4c96-83bf-ac0adcb0c986
2024-12-09 15:24:04.319074: c11edd65-a835-4c96-83bf-ac0adcb0c986
2024-12-09 15:24:09.322712: c11edd65-a835-4c96-83bf-ac0adcb0c986 
```

