#!/usr/bin/env python

import sh


def install_packages(packages_lst):
    for p in packages_lst:
        sh.apt_get("install", "-y", p)


def install_docker():
    # Here should pe piping like sh.sh(sh.curl("-sSL", "https://get.docker.com/", _out="docker_script.sh")),
    # but it doesn't work. Why?
    sh.curl("-sSL", "https://get.docker.com/", _out="docker_script.sh")
    sh.sh("docker_script.sh")
    sh.rm("docker_script.sh")


if __name__ == '__main__':
    install_packages(["curl", "vim"])
    install_docker()
    print "Docker is installed"