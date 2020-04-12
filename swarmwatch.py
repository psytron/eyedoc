


import docker
import time

client = docker.from_env()


while True:
    print('\nCluster Update: ')
    for container in client.containers.list():
        con = client.containers.get( container.id )
        try:
            print( '' )
            print( '          container: ', container.id[:6] )
            print( ' wants traffic from: ', con.labels['com.roo.domain'] )
            print( '    is listening on: ', [ x for x in con.ports ] ,'\n')
        except Exception as e:
            pass

    time.sleep(5)