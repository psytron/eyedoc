


import docker


client = docker.from_env()
clientAPI = docker.APIClient(base_url='unix://var/run/docker.sock')


# SWARM CONTAINER SEARCH
for t in clientAPI.tasks( {'desired-state':'running'}):
    tsk = clientAPI.inspect_task( t['ID'] )
    try:
        detected_domain = tsk['Spec']['ContainerSpec']['Labels']['com.roo.domain']
        print('domain found: ', detected_domain )
        print('container IP: ', tsk['NetworksAttachments'][0]['Addresses'] )
        node = clientAPI.inspect_node( tsk['NodeID'] )
        ip = node['Status']['Addr']
        print('     Node IP: ', ip )
    except Exception as e:
        print(' no domain ')





def inspect_node_iter():
    l = clientAPI.inspect_swarm()  # WORKS for SWARM INFO
    nodez = clientAPI.nodes()
    for n in nodez:
        l=n
        nodeID = n['ID']
        g = clientAPI.inspect_node( nodeID )
        nodeIP = g['Status']['Addr']
        print(' NODE: ', nodeID , ' : ',nodeIP)
        f=3



# PROXY ?
# cli = Client(base_url='tcp://127.0.0.1:2375')
# cli.containers()




# list container IDs per service:
# for f in $(docker service ps -q my-ngx -f desired-state=running);do docker inspect --format '{{.Status.ContainerStatus.ContainerID}}' $f; done

# client.swarm.init(
#     advertise_addr='eth0', listen_addr='0.0.0.0:5000',
#     force_new_cluster=False, default_addr_pool=['10.20.0.0/16],
#     subnet_size=24, snapshot_interval=5000,
#     log_entries_for_slow_followers=1200 )
#


