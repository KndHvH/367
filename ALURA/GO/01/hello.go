package main

import (
	"fmt"
	"strconv"
	"reflect"
)

func helloworld() {
	fmt.Println("Hello, World!")
}

func var_helloworld() {
	var nome string = "Matias"
	var idade int = 22
	numero := 10
	fmt.Println("Hello, " + nome + "!")
	fmt.Println(strconv.Itoa(idade) + " Anos!")
	fmt.Println("Anos:", idade)
	fmt.Println("Tipo da variável numero:", reflect.TypeOf(numero))
}

func main() {
	helloworld()
	var_helloworld()
}