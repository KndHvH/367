package main

import (
	"fmt"
	"os"
)

func main() {
	welcome()
	showMenu()
	option := getOption()

	// fmt.Println("O valor da opção escolhida foi:", option)

	switch option {
	case 1:
		fmt.Println("Iniciando Monitoramento...")
	case 2:
		fmt.Println("Exibindo Logs...")
	case 0:
		fmt.Println("Saindo do Programa...")
		os.Exit(0)
	default:
		fmt.Println("Opção Inválida")
	}

}

func welcome() {
	name := "Matias"
	version := 1.1

	fmt.Println("Hello,", name)
	fmt.Println("Version:", version)
}

func showMenu() {
	fmt.Println("1 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir Logs")
	fmt.Println("0 - Sair do Programa")
}

func getOption() int {
	fmt.Print("Digite o numero: ")
	option := -1
	fmt.Scan(&option)
	return option
}
