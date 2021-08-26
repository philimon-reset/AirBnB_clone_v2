#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"


def do_clean(number=0):
    """deletes out-of-date archives,
    """
    target = sudo('ls -t ./AirBnB_Clone_V2/versions').split()
    if number == 0 or number == 1:
            cleanup = target[1:]
            for i in range(len(cleanup)):
                    sudo('rm /data/web_static/releases/{}'.format(cleanup[i].strip(".tgz")))
