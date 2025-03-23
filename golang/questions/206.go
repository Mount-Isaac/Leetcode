/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package questions

import "fmt"

func ReverseList(head *ListNode) *ListNode {
	current := head
	var prev *ListNode

	if current == nil {
		return head
	}
	for current != nil {
		nextNode := current.Next
		current.Next = prev
		prev = current
		current = nextNode
	}
	return prev

}

func PrintNodes(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, "->")
		head = head.Next
	}
	fmt.Println("nil")
}
