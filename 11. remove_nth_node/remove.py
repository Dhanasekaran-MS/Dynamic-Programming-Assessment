###  Program

# def length(head):
#     i=0
#     thead = head
#     while thead != None:
#         i+=1
#         thead = thead.next
#     return i

# def removeNthFromEnd(self, head, n):
#     nodes = length(head)
#     # n==nodes (first node)
#     if n==nodes:
#         return head.next
#     thead = head
#     # moves before to reach the nth node from last
#     moves = nodes-n-1

#     while moves>0:
#         moves-=1
#         thead = thead.next
#     # if the next node of nth node is not None just replacing the prev next to further next
#     # cuts the pointer of nth node
#     if thead.next != None:
#         thead = thead.next.next

#     return head

### Visualize  
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def length(self, head):
        i = 0
        thead = head
        while thead is not None:
            i += 1
            thead = thead.next
        return i

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = self.length(head)
        
        # Special case: Removing the head node
        if n == nodes:
            return head.next
        
        thead = head

        # Traverse to the (nodes - n - 1)th node
        moves = nodes - n - 1
        while moves > 0:
            moves -= 1
            thead = thead.next
        
        # Remove the nth node from the end
        if thead.next is not None:
            thead.next = thead.next.next
        
        return head

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
print_list(head)
print("n = 2")
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)
print_list(new_head)  # Output should be: 1 -> 2 -> 3 -> 5 -> None
