from fabric.api import *
def hello():
    target = run('ls | xargs stat | grep "Change" | cut -d " " -f 2,3')
    print(target)

