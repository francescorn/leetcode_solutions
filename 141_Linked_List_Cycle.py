class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        while head is not None:
            if head in dictionary:
                return True
            dictionary[head] = head.val
            head = head.next
