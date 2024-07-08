'''
1823. Find the Winner of the Circular Game
Medium

Question:
    There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

    The rules of the game are as follows:

    Start at the 1st friend.
    Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
    The last friend you counted leaves the circle and loses the game.
    If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
    Else, the last friend in the circle wins the game.
    Given the number of friends, n, and an integer k, return the winner of the game.

Example:
    Input: n = 5, k = 2
    Output: 3
    Explanation: Here are the steps of the game:
    1) Start at friend 1.
    2) Count 2 friends clockwise, which are friends 1 and 2.
    3) Friend 2 leaves the circle. Next start is friend 3.
    4) Count 2 friends clockwise, which are friends 3 and 4.
    5) Friend 4 leaves the circle. Next start is friend 5.
    6) Count 2 friends clockwise, which are friends 5 and 1.
    7) Friend 1 leaves the circle. Next start is friend 3.
    8) Count 2 friends clockwise, which are friends 3 and 5.
    9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Solution:
    simulation:
        - A: uses an index to track the current position and directly removes elements from the list.
            - time: O(n^2), space: O(n)
        - B: simulates the circle by cyclically moving list elements and removing the first element each time.
            - time: O(n^2), space: O(n)
    recursion:
        - C: uses mathematical solution to the Josephus problem, without actually simulating the game process.
             It utilizes the recursive nature of the problem and obtains the result through a simple loop.
            - time: O(n), space: O(1)
'''

class Solution_A:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        
        curr = 0
        length = n
        while len(friends) > 1:
            curr = (curr + (k-1)) % length
            friends.pop(curr)
            length -= 1
            
        return friends[0]

class Solution_B:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        
        while len(friends) > 1:
            # left shift the array with k-1 times
            for _ in range(k-1):
                friends.append(friends.pop(0))
            
            # cut the first one
            friends.pop(0)
            
        return friends[0]

class Solution_C:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        return winner + 1

s = Solution_B()
n = 6
k = 5
print(s.findTheWinner(n, k))  # 1
            