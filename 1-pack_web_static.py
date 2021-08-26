from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime

def do_pack():
        target = local("mkdir -p version")
        name = str(datetime.now()).replace(" ", '')
        opt = re.sub(r'[^\w\s]','', name)
        with tarfile.open("./version/web_static_{}.tgz".format(opt), "w:gz") as tar:
                tar.add('web_static')
        if os.path.exists("./version/web_static_{}.tgz".format(opt)):
                return os.path.normpath("/version/web_static_{}.tgz".format(opt))
        else:
                return None