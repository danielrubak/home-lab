# home-lab

This repository contains the definitions of my home lab services. All of them are running on my Synology 920+ using Docker package from Synology Package Center.

- [home-lab](#home-lab)
  - [Docker Compose specification](#docker-compose-specification)
  - [General](#general)
    - [How to find UID and GID](#how-to-find-uid-and-gid)
    - [How to get TZ](#how-to-get-tz)
  - [Heimdall](#heimdall)
  - [n8n](#n8n)
    - [flyway](#flyway)
  - [Nginx Proxy Manager](#nginx-proxy-manager)
  - [Pihole](#pihole)
  - [Portainer](#portainer)
    - [Update the Portainer container](#update-the-portainer-container)
  - [Unifi Controller](#unifi-controller)
  - [Calibre](#calibre)
    - [Calibre Server config](#calibre-server-config)
    - [Calibre Web config](#calibre-web-config)
    - [Link the shared folder](#link-the-shared-folder)
    - [Enable Calibre Server auto-merge](#enable-calibre-server-auto-merge)

## Docker Compose specification

The following elements are used in the docker compose config files:

| Element        | Description                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------- |
| image          | Specifies the image to start the container from                                                   |
| container_name | Specifies a custom container name                                                                 |
| networks       | Defines the networks that service containers are attached to                                      |
| network_mode   | Sets service containers network mode                                                              |
| command        | Overrides the default command declared by the container image                                     |
| ports          | Exposes container ports                                                                           |
| environment    | Defines environment variables set in the container                                                |
| volumes        | Defines mount host paths or named volumes that MUST be accessible by service containers           |
| restart        | Defines the policy that the platform will apply on container termination                          |
| depends_on     | Expresses startup and shutdown dependencies between services                                      |
| healthcheck    | Declares a check that’s run to determine whether or not containers for this service are “healthy” |

More information about other elements you can find in [Compose Specification](https://docs.docker.com/compose/compose-file/).

## General

### How to find UID and GID

- SSH to your server

  ```bash
  ssh username@synology-ip
  ```

- get user ID and group ID

  ```bash
  id
  ```

### How to get TZ

You can find your timezone [here](https://timezone.mariushosting.com/).

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

**NOTE!** Because Synology runs docker containers using non root user, you have to change permissions to the `file` folder using following command:

```bash
sudo chmod 777 -R /volume1/docker/n8n/files
```

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
| TZ                | container timezone                                                             |

### flyway

Flyway is a database migration tool. You can find more information [here](https://flywaydb.org/documentation/)

## Nginx Proxy Manager

Nginx Proxy Manager is a reverse proxy, can be used to redirects the url requests to provided locations.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- nginx-proxy
|   |-- data
|   |-- db
|   |-- letsencrypt
```

Purpose of above directory structure:

- data - nginx proxy manager service configuration
- db - all database related stuff will be stored here
- letsencrypt - folder for your certificates

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable             | Description                |
| -------------------- | -------------------------- |
| NPM_DB_ROOT_PASSWORD | mariadb root user password |
| NPM_DB_USER          | mariadb default user       |
| NPM_DB_USER_PASSWORD | mariadb default password   |
| NPM_DB_NAME          | mariadb database name      |

## Pihole

Pi-hole is an application for blocking advertisements and a DNS server.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- pihole
|   |-- dnsmasq.d
|   |-- pihole
```

Purpose of above directory structure:

- dnsmasq.d - DNS configuration
- pihole - pihole configuration

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable            | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| PIHOLE_UID          | process user ID                                                   |
| PIHOLE_GID          | process group ID                                                  |
| PIHOLE_PASSWORD     | pihole password                                                   |
| PIHOLE_VIRTUAL_HOST | pihole hostname for get access to the service using reverse proxy |
| PIHOLE_WEBPORT      | web app port                                                      |

## Portainer

Portainer is a self-service container service delivery platform. It is the definitive container management GUI for Kubernetes, Docker and Swarm.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- portainer
|   |-- data
|   |-- docker-compose.yml
```

### Update the Portainer container

Follow the steps:

- Connect to the Synology using ssh:

  ```bash
  ssh username@SYNOLOGY_IP -p PORT_NUMBER
  ```

- Run the command below to get the container ID for Portainer

  ```bash
  sudo docker container ls
  ```

- Run the command below to stop the Portainer container

  ```bash
  sudo docker stop portainer
  # if the command above does not work, stop the container using the container ID
  sudo docker stop [CONTAINER_ID]
  ```

- Delete the Portainer container

  ```bash
  sudo docker rm portainer
  # if the command above does not work, remove the container using the container ID
  sudo docker rm [CONTAINER_ID]
  ```

- If you want to update container to the higher minor/major version, remove the portainer image:

  ```bash
  sudo docker rmi <IMAGE_ID>
  ```

- Change your current working directory

  ```bash
  cd /volume1/docker/portainer
  ```

- Use Docker Compose to run new Portainer container

  ```bash
  sudo docker-compose up -d
  ```

## Unifi Controller

Unifi Controller is a software for Unifi devices management. It is required to configure and maintain the network, adopt new devices and manage the WiFi networks and Access Points.

Before installing, you need to create a following directory structure in the docker folder:

```bash
.
|-- unifi-controller
```

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable | Description        |
| -------- | ------------------ |
| PUID     | process user ID    |
| PGID     | process group ID   |
| TZ       | container timezone |

## Calibre

Calibre is an e-book manager. It can view, convert, edit and catalog e-books in all of the major e-book formats.
Calibre-Web is a web app providing a clean interface for browsing, reading and downloading eBooks using a valid Calibre database.

```bash
.
|-- calibre
|   |-- server
|   |   |-- books
|   |   |-- shared
|   |-- web
```

Purpose of above directory structure:

- server - calibre server configuration
- books - directory for storing ebooks database
- shared - symbolic link to the "raw" ebooks directory (optional)
- web - calibre web client configuration

Additionally, service setup requires few environment variables. All of them you can find in the `.dev.env` file. Change the values of these variables and a name of the file to `.env`.

| Variable | Description        |
| -------- | ------------------ |
| PUID     | process user ID    |
| PGID     | process group ID   |
| TZ       | container timezone |

### Calibre Server config

1. Go to the address: <http://HOST_IP:8082>
2. Change the library location to `/config/books`
3. Select your default ebook device

### Calibre Web config

1. Go to the address: <http://HOST_IP:8083>
2. Login using `admin` login and `admin123` password
3. Change the location of Calibre Database to `/books` and click Save
4. Change the default `admin` password in the profile page and click Save

### Link the shared folder

1. Login to your server using SSH
2. Create symbolic link from your ebooks directory to the `shared` folder

```bash
sudo mount --bind path/to/ebooks path/to/shared
# on Synology you can use sth like this
sudo mount --bind path/to/ebooks /volume1/docker/calibre/server/shared
```

### Enable Calibre Server auto-merge

1. Go to the address: <http://HOST_IP:8082>
2. Select `Preferences` from the toolbar, go to `Adding books`, switch to `Adding actions` tab
3. Check option `Auto-merge added books if they already exists
