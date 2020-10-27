package main
import (
	"fmt"
	"sync"
)

func main(){
	NUMLOOPS:=10
	var wg sync.WaitGroup

	fmt.Println("Lets try printing hello world in",NUMLOOPS,"threads")
	fmt.Println("I wonder which one will print first:")
	var i int=0

	for i<NUMLOOPS{
		wg.Add(1)
	
		go func(i int){
			defer wg.Done()
			fmt.Println(i+1,"Hello World")
		}(i)
	
		i+=1
	}
	wg.Wait()
}
