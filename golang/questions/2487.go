package questions

import "fmt"

func RemoveNodesLList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	var stack []*ListNode
	// var maxNumber *ListNode
	current := head

	for current != nil {
		stack = append(stack, current)
		current = current.Next
	}
	println("stack: ", stack)

	for len(stack) > 0 {
		fmt.Println(stack[len(stack)])
	}
	return stack[0]
}
