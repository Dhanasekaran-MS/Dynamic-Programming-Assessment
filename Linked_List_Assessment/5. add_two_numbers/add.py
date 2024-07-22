from typing import Optional

# LOGIC
# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     dummy = ListNode()
#     current = dummy
#     carry = 0

#     while l1 or l2 or carry:
#         val1 = l1.val if l1 else 0
#         val2 = l2.val if l2 else 0
#         total = val1 + val2 + carry
#         carry = total // 10
#         current.next = ListNode(total % 10)
#         current = current.next

#         if l1:
#             l1 = l1.next
#         if l2:
#             l2 = l2.next
    
#     return dummy.next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should be: 7 -> 0 -> 8 -> None

l1 = list_to_linked_list([0])
l2 = list_to_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should be: 0 -> None

l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should be: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None
