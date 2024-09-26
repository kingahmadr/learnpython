class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of the merged list
        dummy = ListNode()
        current = dummy
        
        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If any nodes are left in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the next node of dummy, which is the head of the merged list
        return dummy.next