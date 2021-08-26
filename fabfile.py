from fabric.api import *
env.user = 'ubuntu'
env.hosts = ["104.196.155.240"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"
def hello():
    target = run("ls -t .")
    with cd("./versions"):
        target = run('ls -t')
        print(target.split())
