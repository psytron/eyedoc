


import docker
import urllib
import json
import time
import sys

try:
    web_proxy_address = sys.argv[1]
except Exception as e:
    web_proxy_address = 'http://localhost:8851/clusterupdate'
print( 'STARTING EYEDOC with RECEIVE URL: ',web_proxy_address )
client = docker.from_env()
clientAPI = docker.APIClient(base_url='unix://var/run/docker.sock')

while True:
    ### INSPECT UPDATED CONTAINERS
    conz = []
    for container in client.containers.list():
        con = client.containers.get( container.id )
        try:

            inspection_obj = clientAPI.inspect_container( container.id )
            container_networks = inspection_obj['NetworkSettings']['Networks']
            for n in container_networks:
                network_obj = container_networks[n]
                IP_Address = network_obj['IPAddress']
                obj = {
                    'container':container.id,
                    'domain':con.labels['com.roo.domain'],
                    'ports':[ x for x in con.ports ],
                    'ip': IP_Address
                }
                conz.append( obj )

            print( '' )
            print( '          container: ', obj['container'] )
            print( '     expects domain: ', obj['domain'] )
            print( '           on PORTS: ', obj['ports'])
            print( '         IP Address: ', obj['ip'],'\n')

        except Exception as e:
            print( '     expects domain: ','NONE ( NOT PUBLIC ) ')
            pass

    ### POST UPDATED LIST
    params = json.dumps( conz ).encode('utf8')
    req = urllib.request.Request( web_proxy_address , data=params,headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    print(' POSTED TO: ', web_proxy_address , ' : ',params ,' Received: ',response )
    time.sleep(5)