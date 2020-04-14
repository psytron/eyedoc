package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/filters"
	"github.com/docker/docker/client"
	"net/http"
	"time"
)

func main() {

	/////////////// CONNECT TO SOCKET
	ctx := context.Background()
	cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
	if err != nil {
		panic(err)
	}
	taskFilter := filters.NewArgs()
	tasks, err := cli.TaskList(ctx, types.TaskListOptions{Filters: taskFilter})
	fmt.Println(tasks)

	for {
		/////////////////////// SCAN TASKS
		var conz []map[string]string
		for _, task := range tasks {
			if val, ok := task.Spec.ContainerSpec.Labels["com.roo.domain"]; ok {
				for _, ntrk := range task.NetworksAttachments {

					ob := map[string]string{}
					ob["container"] = task.ID
					ob["com.roo.domain"] = val
					ob["receive"] = ntrk.Addresses[0]
					conz = append(conz, ob)
				}
			}
		}

		///////////////////////////// POST MESSAGE TO ROO ABOUT CONTAINERS WITH PUBLIC
		proxy_server_url := "http://localhost:6299/roo/v1/kvs"
		jsonOutbound, _ := json.Marshal(conz)
		fmt.Println(jsonOutbound)
		resp, err := http.Post(proxy_server_url, "application/json", bytes.NewBuffer(jsonOutbound))
		fmt.Println(resp, err)

		//////////////////////////// WAIT FOR SWARM UPDATE
		time.Sleep(5 * time.Second)

	}
}
