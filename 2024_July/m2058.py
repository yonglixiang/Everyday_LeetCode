'''
Question:
    A critical point in a linked list is defined as either a local maxima or a local minima.

    A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

    Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example:
    Input: head = [5,3,1,2,5,1,2]
    Output: [1,3]
    Explanation: There are three critical points:
    - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
    - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
    - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
    The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
    The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Solution:
    - check if a node is critical point
    - calculate the min and max distance
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head) -> list[int]:
        # find which nodes are critical
        criticals = []
        pre_val = None
        curr = head
        position = 1
        while curr.next != None:
            # get current val and next val
            curr_val = curr.val
            next_val = curr.next.val
            
            # check if it is critical
            if pre_val != None and next_val != None:
                if curr_val > pre_val and curr_val > next_val:  # local maximum
                    criticals.append(position)
                elif curr_val < pre_val and curr_val < next_val:  # local minimum
                    criticals.append(position)
            
            # get next previous val
            pre_val = curr.val
            # update loop variable
            curr = curr.next
            position += 1
        
        # calculate the min and max distance
        if len(criticals) < 2:
            return [-1, -1]
        
        max_distance = criticals[-1] - criticals[0]
        min_distance = float('inf')
        for i in range(len(criticals)):
            if i != 0:
                min_distance = min(criticals[i] - criticals[i-1], min_distance)
                
        return [min_distance, max_distance]

end = ListNode(6)
mid_1 = ListNode(10, end)
mid_2 = ListNode(6, mid_1)
mid_3 = ListNode(6, mid_2)
mid_4 = ListNode(9, mid_3)
mid_5 = ListNode(1, mid_4)
mid_6 = ListNode(4, mid_5)
mid_7 = ListNode(8, mid_6)
head = ListNode(6, mid_7)

solution = Solution()
print(solution.nodesBetweenCriticalPoints(head))  # [1,6]
