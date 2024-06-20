# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # first
        node1 = l1
        node2 = l2
        val = (node1.val + node2.val) % 10
        carry = (node1.val + node2.val) // 10
        ans = ListNode(val)
        temp = ans
        
        # middle
        while node1 != None and node2 != None:
            if node1.next == None and node2.next != None:
                node2 = node2.next
                val = (0 + node2.val + carry) % 10
                carry = (0 + node2.val + carry) // 10
                temp.next = ListNode(val)
                temp = temp.next
            elif node1.next != None and node2.next == None:
                node1 = node1.next
                val = (0 + node1.val + carry) % 10
                carry = (0 + node1.val + carry) // 10
                temp.next = ListNode(val)
                temp = temp.next
            elif node1.next != None and node2.next != None:
                node1 = node1.next
                node2 = node2.next
                val = (node1.val + node2.val + carry) % 10
                carry = (node1.val + node2.val + carry) // 10
                temp.next = ListNode(val)
                temp = temp.next
            else:
                node1 = node1.next
                node2 = node2.next
        
        # last
        if carry != 0:
            val = (0 + 0 + carry) % 10
            carry = (0 + 0 + carry) // 10
            temp.next = ListNode(val)
        
        return ans

start_1 = ListNode(9)
index = start_1
for i in range(3):
    index.next = ListNode(9)
    index = index.next

start_2 = ListNode(9)
index = start_2
for i in range(3):
    index.next = ListNode(9)
    index = index.next

solution = Solution()

ans = solution.addTwoNumbers(start_1, start_2)
temp = ans
while temp != None:
    print(temp.val)
    temp = temp.next
