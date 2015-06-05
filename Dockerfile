FROM ubuntu:12.04

MAINTAINER Arseny Sher <sher-ars@yandex.ru>

# Install python with sh module, we will use them for installing cocaine and elliptics
RUN apt-get update && apt-get install -y python && apt-get install -y python-pip && pip install sh

# Install docker
ADD assets/install/install_docker.py /cocaine-setup/install/install_docker.py
RUN chmod 755 /cocaine-setup/install/install_docker.py && /cocaine-setup/install/install_docker.py

# Install cocaine
ADD assets/install/install_cocaine.py /cocaine-setup/install/install_cocaine.py
RUN chmod 755 /cocaine-setup/install/install_cocaine.py && /cocaine-setup/install/install_cocaine.py