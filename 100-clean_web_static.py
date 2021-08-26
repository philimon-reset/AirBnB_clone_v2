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
    if number == 0 or number == 1:
            target = run('ls | xargs stat | grep "Change" | cut -d " " -f 2,3')
