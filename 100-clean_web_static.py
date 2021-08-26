#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"


def do_clean(number=0):
    """deletes out-of-date archives"""
    target = local('ls -t ./versions/').split()
    print(local("pwd"))
    print(len(target), number, target[0])
    if len(target) == 2:
            if number == 0 or number == 1:
                    local('rm -f ./versions/{}'.format(target[-1]))
                    print("here")
                    sudo('rm -rf /data/web_static/releases/{}'.format(target[-1].strip(".tgz")))
            elif number == 2:
                    pass
    elif len(target) > 1:
        if number == 0 or number == 1:
                cl = target[1:]
                for i in range(len(cl)):
                        local('rm -f ./versions/{}'.format(cl[i]))
                        sudo('rm -rf /data/web_static/releases/{}'.format(cl[i].strip(".tgz")))
        elif number == 2:
                cl = target[2:]
                for i in range(len(cl)):
                        local('rm -f ./versions/{}'.format(cl[i]))
                        sudo('rm -rf /data/web_static/releases/{}'.format(cl[i].strip(".tgz")))
    else:
            pass
