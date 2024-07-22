from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head

# Example usage
# Creating a linked list [3, 2, 0, -4] with a cycle at position 1
values = [3, 2, 0, -4]
pos = 1
head = create_linked_list_with_cycle(values, pos)
solution = Solution()
print(solution.hasCycle(head))  # Output should be: True

# Creating a linked list [1, 2] with a cycle at position 0
values = [1, 2]
pos = 0
head = create_linked_list_with_cycle(values, pos)
print(solution.hasCycle(head))  # Output should be: True

# Creating a linked list [1] with no cycle
values = [1]
pos = -1
head = create_linked_list_with_cycle(values, pos)
print(solution.hasCycle(head))  # Output should be: False
