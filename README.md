# home-lab

This repository contains the definitions of my home lab services. All of them are running on my Synology 920+ using Docker package from Synology Package Center.

## Docker Compose

image
container_name
network_mode
ports
environment
volumes
restart

## Heimdall

Heimdall is some kind of a dashboard which organise links to all of my services.

Before installing, you need to create a `heimdall` directory in the docker folder.
It has very simple configuration, all you have to do is type:

```bash
docker-compose up -d
```
