package main

import (
	"fmt"
	"leetcode/testcases"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please specify a question file name to run")
		fmt.Println("Available question files:")

		for _, test := range testcases.GetAvailableTests() {
			fmt.Printf("- %s\n", test)
		}
		return
	}

	fileName := os.Args[1]
	if !testcases.RunTestByFileName(fileName) {
		fmt.Printf("Test for file '%s' not found.\n", fileName)
		fmt.Println("Available question files:")

		for _, test := range testcases.GetAvailableTests() {
			fmt.Printf("- %s\n", test)
		}
	}
}
