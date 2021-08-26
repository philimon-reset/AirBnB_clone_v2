#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = './id_rsa'

def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        base = archive_path.strip('.tgz')
        put(archive_path, '/tmp')
        run('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}/".format(base)
        run('tar -xzf /tmp/{} -C {}'.format(archive_path, main))
        run('rm /tmp/{}'.format(archive_path))
        run('mv {}/web_static/* {}'.format(main, main))
        run('rm -rf /data/web_static/current')
        run('ln -s {} "/data/web_static/current"'.format(main))
        return True
    except:
        return False
