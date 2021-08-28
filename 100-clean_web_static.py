#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"


def do_clean(number=0):
    """deletes out-of-date archives"""
    target = local('ls -t ~/AirBnB_Clone_V2/versions/').split()
    target_R = sudo('ls -t /data/web_static/releases/').split()
    paths = "/data/web_static/releases"
    if len(target) == 2:
        if number == '0' or number == '1':
            local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
            sudo('rm -rf {}/{}'.format(paths, target_R[-1].strip(".tgz")))
        elif number == '2':
            pass
    elif len(target) > 2:
        if number == '0' or number == '1':
            cl = target[1:]
            rem = target_R[1:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
            for j in range(len(rem)):
                sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
        elif number == '2':
            cl = target[2:]
            rem = target_R[2:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
            for j in range(len(rem)):
                sudo(
                    'rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
    else:
        pass
