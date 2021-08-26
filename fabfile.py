from fabric.api import *
env.user = 'ubuntu'
env.hosts = ["104.196.155.240"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"
def hello():
    target = local('ls -t ./versions')
    new = local("pwd")
    print(new)
    print(target.split())
