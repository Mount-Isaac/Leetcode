package testcases

import (
	"fmt"
	"leetcode/questions"
)

// Test function for gcdquestion
func TestGcdQuestion() {
	fmt.Println("========Testing InsertGreatestCommonDivisors========")

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

func ReverseSinglyLList() {
	fmt.Print("========Testing Reversing Singly LinkedList========\n\n")

	//  insert nodes from a slice of elements
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	var head *questions.ListNode
	var current *questions.ListNode

	for _, number := range nums {
		node := &questions.ListNode{Val: number}
		if head == nil {
			head = node
		} else {
			current.Next = node
		}
		current = node
	}
	fmt.Print("Original linked list\n")
	questions.PrintNodes(head)
	reversed_linkedlist := questions.ReverseList(head)
	fmt.Println("\nReversed linked list")
	questions.PrintNodes(reversed_linkedlist)

}
