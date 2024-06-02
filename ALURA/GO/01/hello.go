package main

import (
	"fmt"
	"strconv"
)

func helloworld() {
	fmt.Println("Hello, World!")
}

func var_helloworld() {
	var nome string = "Matias"
	var idade int = 22
	fmt.Println("Hello, " + nome + "!")
	fmt.Println(strconv.Itoa(idade) + " Anos!")
	fmt.Println("Anos:", idade)
}

func main() {
	helloworld()
	var_helloworld()
}