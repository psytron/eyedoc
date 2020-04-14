package eyedoc

import (
	"fmt"
	"context"
	"github.com/docker/docker/client"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/filters"
	//"time"
)

func Tasks() []map[string]string {

	/////////////// CONNECT TO SOCKET
	ctx := context.Background()
	cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
	if err != nil {
		panic(err)
	}
	taskFilter := filters.NewArgs()
	tasks, err := cli.TaskList(ctx, types.TaskListOptions{Filters: taskFilter})
	fmt.Println(tasks)

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


	return conz
}
