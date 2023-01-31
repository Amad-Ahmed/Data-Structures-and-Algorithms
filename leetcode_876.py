
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        mylist = [] # to be used for appending
        itr = head
        while itr:
            length+=1
            itr=itr.next
        # now I know complete length
        mid = int(length/2)
        if (mid % 2 == 0):
            mid = mid+1
        length = 1
        itr = head
        while itr:
            if (length >= mid):
                mylist.append(itr.val)
            length+=1
            itr=itr.next
        
        
        return mylist

# Another method to solve is to use fast and slow pointers
# both initialized to head
# fast =slow = head
# slow = slow.next
# fast = fast.next.next
# when fast reaches end of list, slow will be at middle