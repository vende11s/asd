'''
Napisac merge z mergesorta
'''

class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def mergeSortedLinkedLists(head1, head2):
    dummy = Node()
    tail = dummy

    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            tail = head1
            head1 = head1.next
        else:
            tail.next = head2
            tail = head2
            head2 = head2.next
    if head1:
        tail.next = head1
    if head2:
        tail.next = head2

    while tail.next is not None:
        tail = tail.next

    return (dummy.next, tail)