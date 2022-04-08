package main

import "fmt"



func main() {
	var s string
	fmt.Scan(&s)
	b_count:= 0
	ans := 0
	for _, si := range s {
		if si == 'B'{
			b_count++
		}
		if si == 'W'{
			ans += b_count
		}
	}
	fmt.Println(ans)
}