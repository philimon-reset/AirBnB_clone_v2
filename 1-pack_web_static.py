from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime

def do_pack():
        target = local("mkdir -p version")
        name = str(datetime.now()).replace(" ", '')
        opt = re.sub(r'[^\w\s]','', name)
        with tarfile.open(opt, "w:gz") as tar:
                tar.add('web_static', arcname=os.path.basename('./version'))
        t = tarfile.open(opt, 'r')
        for member in t.getmembers():
                print(member.name)

if __name__ == '__main__':
        do_pack()