import fabric
from fabric import Connection
import tarfile
import os.path
from datetime import datetime

def do_pack():
        target = fabric.local('cat ./web_static')
        with tarfile.open(fabric.local(''), "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
