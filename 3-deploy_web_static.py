#!/usr/bin/python3
        """web server distribution
        """
from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['ubuntu@104.196.155.240', 'ubuntu@34.74.146.120']
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
        """distributes an archive to your web servers
        """
        target = local("mkdir -p versions")
        name = str(datetime.now()).replace(" ", '')
        opt = re.sub(r'[^\w\s]','', name)
        with tarfile.open("./versions/web_static_{}.tgz".format(opt), "w:gz") as tar:
                tar.add('web_static')
        if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
                return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
        else:
                return None

def do_deploy(archive_path):
        """distributes an archive to your web servers
        """
        if os.path.exists(archive_path) == False:
                return False
        try:
                base = archive_path.strip('.tgz')
                put(archive_path, '/tmp')
                run ('mkdir -p /data/web_static/releases/{}'.format(base))
                run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_path, base))
                run('rm /tmp/{}'.format(archive_path))
                run('rm -rf /data/web_static/current')
                run ('ln -s  "/data/web_static/releases/{}/" "/data/web_static/current"'.format(base))
                return True
        except:
                return False

def deploy():
        """distributes an archive to your web servers"""
        path = do_pack()
        if path == None:
                return False
        return do_deploy(path)