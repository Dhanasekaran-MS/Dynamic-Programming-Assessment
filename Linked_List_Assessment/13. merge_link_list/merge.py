# def mergeTwoLists(self, l1: Optional[LinkedNode], l2: Optional[LinkedNode]) -> Optional[LinkedNode]:
#     dummy = LinkedNode(0)
#     current = dummy
#     while l1 and l2:
#         if l1.data < l2.data:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
#     if l1:
#         current.next = l1
#     elif l2:
#         current.next = l2

#     return dummy.next



from typing import Optional

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: Optional[LinkedNode], l2: Optional[LinkedNode]) -> Optional[LinkedNode]:
        # Created a dummy
        dummy = LinkedNode(0)
        current = dummy
        # Traverse through both linked lists and add smaller node to the result list
        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next
        
def list_linkedlist(arr):
    if not arr:
        return None
    head = LinkedNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = LinkedNode(val)
        current = current.next
    return head
    
def linkedlist_list(head):
    results = []
    current = head
    while current:
        results.append(current.data)

        print(current.data, end=' ')
        current = current.next
    print()

ll = list_linkedlist([1,2,3,4])
l2 = list_linkedlist([1,3,5,6])
# print(ll)

linkedlist_list(ll)
linkedlist_list(l2)

sol = Solution()
merged = sol.mergeTwoLists(ll, l2)

linkedlist_list(merged)