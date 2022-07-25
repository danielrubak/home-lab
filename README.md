# home-lab

This repository contains the definitions of my home lab services. All of them are running on my Synology 920+ using Docker package from Synology Package Center.

## Docker Compose

image
container_name
networks
network_mode
command
ports
environment
volumes
restart
depends_on
healthcheck

## Heimdall

Heimdall is some kind of a dashboard which organise links to all of my services.

Before installing, you need to create a `heimdall` directory in the docker folder.
It has very simple configuration, all you have to do is type:

```bash
docker-compose up -d
```

## n8n

n8n is an automation tool, allows to create very complex flows and execute them based on the cron definition or on external triggers.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- n8n
|   |-- db
|   |-- files
|   |-- migrations
|   |-- n8n
```

Purpose of above directory structure:

- db - all database related staff will be stored here
- files - directory for easy exporting files from n8n service
- migrations - folder for future db migration files
- n8n - n8n service configuration

### flyway

Flyway is a database migration tool. You can find more information [here](https://flywaydb.org/documentation/)
