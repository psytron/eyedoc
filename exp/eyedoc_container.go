package exp

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
	"net/http"
	"time"
)

func exp() {

	// CONNECT TO SOCKET
	//ctx := context.Background()
	cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
	if err != nil {
		panic(err)
	}
	containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{})
	if err != nil {
		panic(err)
	}

	// UPDATE
	for {
		// BUILD MAP OF ALL REQUESTED DOMAINS + CONTAINERS:
		var conz []map[string]string
		for _, container := range containers {
			if val, ok := container.Labels["com.roo.domain"]; ok {
				ob := map[string]string{}
				ob["container"] = container.ID
				ob["domain"] = val
				conz = append(conz, ob)
			}
		}

		// SEND CONTAINERS WANTING PUBLIC TRAFFIC TO ROO:
		proxy_server_url := "http://localhost:8851/clusterupdate"
		jsonOutbound, _ := json.Marshal(conz)
		fmt.Println(jsonOutbound)
		resp, err := http.Post(proxy_server_url, "application/json", bytes.NewBuffer(jsonOutbound))
		fmt.Println(resp, err)

		// WAIT 2 SECONDS FOR SWARM UPDATE
		time.Sleep(2 * time.Second)

	}
}
