package main

import "fmt"
import "encoding/json"


func main() {

	proxies []map[string]string
	var proxies := []string{"127.0.0.1:8851", "127.0.0.1:8000" ,"127.0.0.1:8812" }
	for i, s := range strings {
		fmt.Println(i, s)
		obj := map[string]string{}
		obj["domain"]=s
		fmt.Println( obj )
		//conz = append( conz , obj )
	}

	js, _ := json.Marshal( conz )
	fmt.Printf("%s", js)
	fmt.Println(conz)
}