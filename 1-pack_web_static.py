from fabric.api import local
import tarfile
import os.path
from datetime import datetime

def do_pack():
        target = local("mkdir -p version")
        name = datetime.now()
        with tarfile.open('web_static', "w:gz") as tar:
                tar.add(name, arcname=os.path.basename('./version'))
