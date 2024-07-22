# Approach

# def reverse(self, head):
#     prev = None
#     current = head
    
#     while current:
#         next_node = current.next  # Store the next node
#         current.next = prev       # Reverse the current node's pointer
#         prev = current            # Move prev to the current node
#         current = next_node       # Move to the next node
    
#     return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_node       # Move to the next node
        
        return prev  # prev will be the new head of the reversed list

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

s = Solution()
head = list_to_linkedlist([1, 2, 3, 4, 5])
print("Linked List : ",linkedlist_to_list(head))
reversed_head = s.reverseList(head)
print("Reversed : ",linkedlist_to_list(reversed_head)) 