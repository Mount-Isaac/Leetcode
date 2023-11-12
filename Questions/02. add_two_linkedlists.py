class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    def rec(l1, l2, tmp=0):
            
        l1_val = 0 if not l1 else l1.val
        l2_val = 0 if not l2 else l2.val
        
        if l1 or l2 or tmp > 0:
                    
            if l1_val + l2_val + tmp >= 10:
                l1.val = (l1_val + l2_val + tmp) % 10
                tmp = 1
                if not l1.next:
                    l1.next = ListNode(0) 
            else:
                l1.val = l2_val + l1_val + tmp
                tmp = 0
                if l2:
                    if l2.next and not l1.next:
                        l1.next = ListNode(0)

        else:
            return
        rec(l1.next, l2.next if l2 else None, tmp)
            
    rec(l1, l2)
    return l1
        