package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"

	tokenizer "./tokenizer"
)

// Globals
var hadError bool = false

// Error function prints error to the Std Error
func Error(line int, message string) {
	report(line, "", message)
}

func report(line int, where string, message string) {
	fmt.Fprintf(os.Stderr, "[line %d] Error %s : %s", line, where, message)
	hadError = true
}

func run(source string) {
	t := tokenizer.NewToken(tokenizer.EOF, "", "", 23)
	fmt.Println(t.ToString())
}

func runFile(path string) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	run(string(data))
	if hadError {
		os.Exit(65)
	}
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
		hadError = false
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
