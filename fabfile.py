from fabric.api import *
env.user = 'ubuntu'
env.hosts = ["104.196.155.240"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"
def hello():
    target = run('cd AirBnB_Clone_V2/versions')
    t = run('pwd')
    print(t)
    target = run('ls | xargs stat | grep "Change" | cut -d " " -f 2,3 > ../text')
    
