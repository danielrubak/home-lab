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

- db - all database related stuff will be stored here
- files - directory for easy exporting files from n8n service
- migrations - folder for future db migration files
- n8n - n8n service configuration

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable          | Description                                                                    |
| ----------------- | ------------------------------------------------------------------------------ |
| N8N_HOST          | n8n host url or ip                                                             |
| N8N_USER          | n8n default user                                                               |
| N8N_PASSWORD      | n8n default password                                                           |
| N8N_WEBHOOK_URL   | n8n webhook url, will be used to get access to another services, eg google api |
| POSTGRES_DB       | postgres database name                                                         |
| POSTGRES_USER     | postgres default user                                                          |
| POSTGRES_PASSWORD | postgres default password                                                      |

### flyway

Flyway is a database migration tool. You can find more information [here](https://flywaydb.org/documentation/)

## Ngnix Proxy Manager

Ngnix Proxy Manager is a reverse proxy, can be used to redirects the url requests to provided locations.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- ngnix-proxy
|   |-- data
|   |-- db
|   |-- letsencrypt
```

Purpose of above directory structure:

- data - ngnix proxy manager service configuration
- db - all database related stuff will be stored here
- letsencrypt - folder for your certificates

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable             | Description                |
| -------------------- | -------------------------- |
| NPM_DB_ROOT_PASSWORD | mariadb root user password |
| NPM_DB_USER          | mariadb default user       |
| NPM_DB_USER_PASSWORD | mariadb default password   |
| NPM_DB_NAME          | mariadb database name      |
