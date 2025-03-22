package questions

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func InsertGreatestCommonDivisors(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	current := head
	for current != nil && current.Next != nil {
		gcdvalue := gcd(current.Val, current.Next.Val)

		// append a new node
		newNode := &ListNode{
			Val:  gcdvalue,
			Next: current.Next,
		}
		current.Next = newNode
		current = newNode.Next
	}
	return head
}

func CreateListNodes(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	head := &ListNode{Val: nums[0]}
	current := head
	for _, num := range nums[1:] {
		current.Next = &ListNode{Val: num}
		current = current.Next
	}
	return head
}

// Helper to print the linked list
func PrintList(head *ListNode) {
	current := head
	for current != nil {
		fmt.Printf("%d ", current.Val)
		current = current.Next
		if current != nil {
			fmt.Print("-> ")
		}
	}
	fmt.Println()
}
