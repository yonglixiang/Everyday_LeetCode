'''
2181. Merge Nodes in Between Zeros
Medium

Question:
    You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

    For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

    Return the head of the modified linked list.

Example:
    Input: head = [0,3,1,0,4,5,2,0]
    Output: [4,11]
    Explanation: 
    The above figure represents the given linked list. The modified list contains
    - The sum of the nodes marked in green: 3 + 1 = 4.
    - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Solution:
    time complexity: O(n)
    memory complexity: O(1)
    - Create a merged node when you reach the node with the value 0. 
    - When creating a new node, update the merge_val and node.next. 
    - Be careful about the head node.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeNodes(self, head):
        curr = head.next
        node = None
        merge_val = 0
        
        while curr != None:
            if curr.val == 0:
                if node is None:
                    merge_head = ListNode(merge_val)
                    node = merge_head
                else:
                    node.next = ListNode(merge_val)
                    node = node.next
                merge_val = 0
            else:
                merge_val += curr.val
            
            curr = curr.next
        
        return merge_head

[0,3,1,0,4,5,2,0]
end = ListNode(0)
mid_1 = ListNode(2, end)
mid_2 = ListNode(5, mid_1)
mid_3 = ListNode(4, mid_2)
mid_4 = ListNode(0, mid_3)
mid_5 = ListNode(1, mid_4)
mid_6 = ListNode(3, mid_5)
head = ListNode(0, mid_6)

solution = Solution()
merge_head = solution.mergeNodes(head)

curr = merge_head
while curr != None:
    print(curr.val)
    curr = curr.next