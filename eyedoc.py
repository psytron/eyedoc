


import docker
import time

client = docker.from_env()
clientAPI = docker.APIClient(base_url='unix://var/run/docker.sock')

while True:
    for container in client.containers.list():
        con = client.containers.get( container.id )
        try:

            inspection_obj = clientAPI.inspect_container( container.id )
            container_networks = inspection_obj['NetworkSettings']['Networks']
            for n in container_networks:
                network_obj = container_networks[n]
                IP_Address = network_obj['IPAddress']
            print( '' )
            print( '          container: ', container.id[:5] )
            print( '     expects domain: ', con.labels['com.roo.domain'] )
            print( '           on PORTS: ', [ x for x in con.ports ] )
            print( '         IP Address: ', IP_Address ,'\n')

        except Exception as e:
            print( '     expects domain: ','NONE ( NOT PUBLIC ) ')
            pass

    time.sleep(5)