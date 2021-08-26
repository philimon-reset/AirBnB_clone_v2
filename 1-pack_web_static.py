from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime

def do_pack():
        target = local("mkdir -p versions")
        name = str(datetime.now()).replace(" ", '')
        opt = re.sub(r'[^\w\s]','', name)
        with tarfile.open("./versions/web_static_{}.tgz".format(opt), "w:gz") as tar:
                tar.add('web_static')
        if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
                return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
        else:
                return None