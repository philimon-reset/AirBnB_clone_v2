from fabric.api import *
import os.path

def do_deploy(archive_path):
        env.hosts = ['ubuntu@104.196.155.240', 'ubuntu@34.74.146.120']
        if os.path.exists(archive_path) == False:
                return False
        base = archive_path.strip('.tgz')
        put(archive_path, '/tmp/')
        run ('mkdir -p /data/web_static/releases/{}'.format(base))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_path, base))
        run('rm /tmp/{}'.format(archive_path))
        run('rm -rf /data/web_static/current')
        run ('ln -s  "/data/web_static/releases/{}/" "/data/web_static/current"'.format(base))