#!/usr/bin/env python

import sh

from install_docker import install_packages


def add_reverbrain_repos():
    # there is no docker plugin package in trusty repos, hmm...
    # ok, let's try trusty. hope that docker plugin is integrated into libcocaine-core2
    repos = """\
    deb http://repo.reverbrain.com/trusty/ current/amd64/
    deb http://repo.reverbrain.com/trusty/ current/all/
    """
    with open("/etc/apt/sources.list.d/reverbrain.list", "a") as f:
        f.write(repos)
    sh.apt_key(sh.curl("http://repo.reverbrain.com/REVERBRAIN.GPG"), "add", "-")
    sh.apt_get("-y", "update")


def install_cocaine():
    COCAINE_VERSION = "0.11.3.2"
    # COCAINE_VERSION = "0.11.2.5"
    # there is no libcocaine-plugin-docker2=0.11.3.2 package in precise repo,
    # and no docker package in trusty repo at all
    # ok, let's install cocaine 0.11.3.2 on trusty hoping that docker plugin is integrated into one of the packages
    # Issue something like cocaine-runtime -c /cocaine-setup/conf/cocaine-local.conf -d to start the daemon
    # apt-get install libcocaine-core2 cocaine-runtime msgpack-python build-essential python-dev cocaine-tools
    install_packages(["libcocaine-core2=%s" % COCAINE_VERSION, "cocaine-runtime=%s" % COCAINE_VERSION,
                      # "libcocaine-plugin-docker2=%s" % COCAINE_VERSION,
                      "msgpack-python", "build-essential", "python-dev"])
    sh.pip("install", "cocaine-tools")


def install_elliptics():
    ELLIPTICS_VERSION = "2.25.6.4"

if __name__ == '__main__':
    add_reverbrain_repos()
    install_cocaine()
    install_elliptics()
    # print "Cocaine is installed"