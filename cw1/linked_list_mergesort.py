class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def merge(l1,l2):
    res = Node(0)
    tail = res

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            tail = l1
            l1 = l1.next
        else:
            tail.next = l2
            tail = l2
            l2 = l2.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return res.next


def findMiddle(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSort(head):
    if not head or not head.next:
        return head

    temp = findMiddle(head)
    left = head
    right = temp.next

    temp.next = None

    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)



l = Node(2)
l.next = Node(1)
l.next.next = Node(3)
l.next.next.next = Node(7)
l.next.next.next.next = Node(4)

l = mergeSort(l)

while l:
    print(l.val)
    l = l.next