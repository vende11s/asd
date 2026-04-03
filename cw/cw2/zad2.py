'''
Proszę zaimplementować funkcje odrywającą serię naturalną z linked listy
'''

class Node:
    def __init__(self):
        self.val = 0
        self.next = None

def solution(head1):
    if not head1:
        return None
    
    while head1.next:
        if head1.val > head1.next.val:
            temp = head1.next
            head1.next = None
            return temp
        