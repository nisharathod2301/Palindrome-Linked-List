# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastptr = head
        slowptr = head
        
        #find middle
        while fastptr and fastptr.next:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            
        #reverse the second half
        prev = None
        while slowptr:
            temp = slowptr.next
            slowptr.next = prev
            prev = slowptr
            slowptr = temp
            
        #Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right .next
        return True
            
            
