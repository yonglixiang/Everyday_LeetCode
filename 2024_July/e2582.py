'''
2582. Pass the Pillow
Easy

Question:
    There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

    For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
    Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

Example:
    Input: n = 4, time = 5
    Output: 2
    Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
    After five seconds, the 2nd person is holding the pillow.

Solution:
    curr: current people who hold the pillow, start with 1. 
    direction: the direction of passing, left = 1, right = -1. Start with 1, change to opposite when reach leftest and rightest
'''

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr = 1
        direction = 1
        
        for _ in range(time):
            if curr == 1:
                direction = 1
            elif curr == n:
                direction = -1
            
            curr += direction
        
        return curr

solution = Solution()
n = 4
time = 5
print(solution.passThePillow(n, time))  # 2
        
        