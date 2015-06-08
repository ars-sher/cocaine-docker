FROM ubuntu:14.04

MAINTAINER Arseny Sher <sher-ars@yandex.ru>

# Install python with sh module, we will use them for installing cocaine and elliptics
RUN apt-get update && apt-get install -y python && apt-get install -y python-pip && pip install sh

# Install docker
# Remember that you MUST run the outer container with --privileged flag or it won't work.
# Docker can be started as "service docker start", but since we use supervisor we will run magic wrapper from
# https://registry.hub.docker.com/u/jpetazzo/dind/
# Tested on Trusty, but Saucy should work too. Precise will not since it has old kernel.
ADD assets/install/install_docker.py /cocaine-setup/install/install_docker.py
RUN chmod 755 /cocaine-setup/install/install_docker.py && /cocaine-setup/install/install_docker.py
# Add magic wrapper for starting Docker daemon by supervisor
ADD assets/install/wrapdocker.sh /cocaine-setup/install/wrapdocker.sh
RUN chmod +x /cocaine-setup/install/wrapdocker.sh

# Install cocaine
ADD assets/install/install_cocaine.py /cocaine-setup/install/install_cocaine.py
RUN chmod 755 /cocaine-setup/install/install_cocaine.py && /cocaine-setup/install/install_cocaine.py

# Install supervisor
RUN apt-get update && apt-get install -y supervisor
ADD assets/conf/supervisord.conf /cocaine-setup/conf/supervisord.conf

# Add configs and start daemons
#ADD assets/conf/ /cocaine-setup/conf/
#ADD assets/init.py /cocaine-setup/init.py
#RUN mkdir /var/run/cocaine/
    #&& chmod 755 /cocaine-setup/init.py && /cocaine-setup/init.py

CMD ["/usr/bin/supervisord", "-c", "/cocaine-setup/conf/supervisord.conf"]

#CMD ["cocaine-runtime", "-c", "/cocaine-setup/conf/cocaine-local.conf"]
#CMD ["tail", "-f", "/var/log/cocaine"]
