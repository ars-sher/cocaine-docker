## About

This is a Dockerfile for building local virtual Cocaine 0.11.3.2 cloud. The image is based on Ubuntu Trusty.

Main commands:
To build the image, issue something like
```
sudo docker build -t sher/trusty-cocaine .
```

To run the container, do
```
sudo docker run --privileged -t -i --rm --name cocs sher/trusty-cocaine
```
. --privileged here is necessary to make docker-in-docker work.

Then you will have a running container with working cocaine and docker daemons. It is easy to open terminal session
with the container by
```
sudo docker exec -it cocs bash
```

## Isolation
Currently only as a process; TODO: configure and test Docker

## Data Store
Currently only local; TODO: install, configure and test elliptics