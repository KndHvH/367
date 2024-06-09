package main

import (
	"fmt"
)

func main() {
	name := "Matias"
	version := 1.1
	option := 0

	fmt.Println("Hello,", name)
	fmt.Println("Version:", version)

	fmt.Println("1 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir Logs")
	fmt.Println("0 - Sair do Programa")

	fmt.Scanf("%d", &option)
}