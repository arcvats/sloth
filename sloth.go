package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func run(source string) {
	fmt.Println(source)
}

func runFile(path string) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	run(string(data))
}

func runPrompt() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Print("sloth> ")
		line, err := reader.ReadString('\n')
		if err != nil {
			panic(err)
		}
		if strings.TrimSpace(line) == "exit()" {
			os.Exit(0)
		}
		run(line)
	}
}

func main() {
	var arguments []string = os.Args[1:]

	if argumentsLength := len(arguments); argumentsLength > 1 {
		fmt.Println("Usage: sloth [script]")
		os.Exit(64)
	} else if argumentsLength == 1 {
		runFile(arguments[0])
	} else {
		runPrompt()
	}
}
