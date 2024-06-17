package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	welcome(get_name_and_version())
	for {
		showMenu()
		option := getOption()

		fmt.Println("O valor da opção escolhida foi:", option)

		switch option {
		case 1:
			initMonitoring()
		case 2:
			fmt.Println("Exibindo Logs...")
		case 0:
			fmt.Println("Saindo do Programa...")
			os.Exit(0)
		default:
			fmt.Println("Opção Inválida")
		}

	}

}

// Returns a name and a version, like Matias and 1.1
func get_name_and_version() (string, float64) {
	name := "Matias"
	version := 1.1
	return name, version
}

// Prints a welcome message, with the name and version
func welcome(name string, version float64) {
	fmt.Println("Hello,", name)
	fmt.Println("Version:", version)
}

// Shows the menu options
func showMenu() {
	fmt.Println("--------------------")
	fmt.Println("1 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir Logs")
	fmt.Println("0 - Sair do Programa")
	fmt.Println("--------------------")
}

// Gets the option from the user, and returns it
func getOption() int {
	fmt.Print("Digite o numero: ")
	option := -1
	fmt.Scan(&option)
	return option
}

func initMonitoring() {
	fmt.Println("Iniciando Monitoramento...")
	site := "https://httpbin.org/status/404"
	response, _ := http.Get(site)
	if response.StatusCode == 200 {
		fmt.Println("Site:", site, "foi carregado com sucesso!")
	} else {
		fmt.Println("Site:", site, "esta com problemas. Status Code:", response.StatusCode)
	}
}
