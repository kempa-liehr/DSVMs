# SePiaPro VMs

## Requirements
* vagrant
* ansible >= 2.0

## Directory structure
* single contains a vagrant setup for one machine running flink locally.
* cluster contains a vagrant setup for two machines that form a minimal flink cluster

## Quick start
```bash
$ git clone ssh://git@code.blue-yonder.org:7999/sepiapro/sepiapro_vms.git
$ cd sepiapro_vms/single
$ vagrant up
```

Apache Flink is now up and running. You can access the Web Dashboard via http://localhost:9091

To run flink programms, enter the vm:

```bash
$ vagrant ssh
$ pyflink2.sh examples/local_mae.py
$ cat result.txt
```

## Cluster
```bash
$ git clone ssh://git@code.blue-yonder.org:7999/sepiapro/sepiapro_vms.git
$ cd sepiapro_vms/cluster
$ ./setup.sh  # generate ssh keys
$ vagrant ssh
$ pyflink2.sh examples/cluster_mae.py
$ ssh slave
$ cat result.txt
```
