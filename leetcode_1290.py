# traverse whole list and store it in a string along with calculation of length

# then traverse through each character and convert accordingly
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ""
        length = 0
        itr = head
        while itr:
            num = num + str(itr.val)
            length+=1
            itr=itr.next
        
        decimal = 0
        for i in range(len(num)):
            decimal = decimal + (int(num[i])*(2**length))
            length-=1

        return decimal


        

        