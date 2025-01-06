class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      middle = head
      end = head
      while end and end.next:  # applicable until we reach the end of the linked list
        middle = middle.next # middle node moves by 1
        end = end.next.next #end node moves by 2.
      return middle
