package testcases

import (
	"strings"
)

// Map file names to their test functions
var fileToTestFunc = map[string]func(){
	"2807": TestGcdQuestion,
}

// runs a test based on the file name
func RunTestByFileName(fileName string) bool {
	fileName = strings.TrimSuffix(fileName, ".go")
	fileName = strings.ToLower(fileName)

	// get test function
	if testFunc, exists := fileToTestFunc[fileName]; exists {
		testFunc()
		return true
	}

	return false
}

// returns list of available test file names
func GetAvailableTests() []string {
	tests := make([]string, 0, len(fileToTestFunc))
	for name := range fileToTestFunc {
		tests = append(tests, name)
	}
	return tests
}
