package testcases

import (
	"fmt"
	"leetcode/questions"
)

// Test function for gcdquestion
func TestGcdQuestion() {
	fmt.Println("Testing InsertGreatestCommonDivisors:")

	// Test case 1
	nums := []int{18, 6, 10, 3}
	head := questions.CreateListNodes(nums)
	fmt.Print("Original list: ")
	questions.PrintList(head)

	result := questions.InsertGreatestCommonDivisors(head)
	fmt.Print("After inserting GCDs: ")
	questions.PrintList(result)

	// Test case 2
	nums2 := []int{7, 21, 14}
	head2 := questions.CreateListNodes(nums2)
	fmt.Print("\nOriginal list: ")
	questions.PrintList(head2)

	result2 := questions.InsertGreatestCommonDivisors(head2)
	fmt.Print("After inserting GCDs: ")
	questions.PrintList(result2)
}
