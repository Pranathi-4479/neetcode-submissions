class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head

        while curr and curr.next:

            prev = curr
            last = curr.next

            while last.next:
                prev = last
                last = last.next


            prev.next = None

            last.next = curr.next
            curr.next = last
            curr = last.next