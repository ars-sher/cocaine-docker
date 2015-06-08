#!/usr/bin/env python

import sh


def run_cocaine():
    # specify path to cocaine conf here
    conf_path = "/cocaine-setup/conf/cocaine-local.conf"
    # doesn't work for now
    # sh.cocaine_runtime("-c", conf_path, "-d")

if __name__ == '__main__':
    run_cocaine()
    print "Cocaine is up and running!"