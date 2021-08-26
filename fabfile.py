from fabric.api import *
env.user = 'ubuntu'
env.hosts = ["104.196.155.240"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"
def hello():
    with lcd("./versions"):
        target = local('ls -t')
        new = local("pwd")
        print(new)
        print(target.split())
