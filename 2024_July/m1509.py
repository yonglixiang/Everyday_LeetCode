'''
Question:
    You are given an integer array nums.
    In one move, you can choose one element of nums and change it to any value.
    Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

Example:
    Input: nums = [5,3,2,4]
    Output: 0
    Explanation: We can make at most 3 moves.
    In the first move, change 2 to 3. nums becomes [5,3,3,4].
    In the second move, change 4 to 3. nums becomes [5,3,3,3].
    In the third move, change 5 to 3. nums becomes [3,3,3,3].
    After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

Solution: sliding window.
    step1: sort
    step2: enumerate all possible ways to do X times move, calculate diff respectively.(sliding window)
        For 3 times move, there are 4 ways to make moving(take 1,3,4,7,8,10 as example)
        - 0 left, 3 right(1,3,4 left, diff = 3)
        - 1 left, 2 right(3,4,7 left, diff = 6)
        - 2 left, 1 right(4,7,8 left, diff = 4)
        - 3 left, 0 right(7,8,10 left, diff = 3)
    step3: find the minimum way and return
    
    edge condition: len(nums) <= X+1, always return 0
    advanced: we should only focus on min X+1 and max X+1 elements among a large list

'''

class SolutionA():
    def minDifference(self, nums: list[int]) -> int:
        # define move times
        N = 3
        if len(nums) <= N+1:
            return 0
        
        nums.sort()
        
        # sliding window
        res = float('inf')
        for i in range(N + 1):
            l = i
            r = -1-(N-i)
            res = min(
                res, nums[r] - nums[l]
            )
        
        return res

import heapq
class SolutionB():
    def minDifference(self, nums: list[int]) -> int:
        # define move times
        times = 3
        if len(nums) <= times+1:
            return 0
        
        # only focus on min X + 1 elements and max X + 1 elements
        min_four = sorted(heapq.nsmallest(times+1, nums))
        max_four = sorted(heapq.nlargest(times+1, nums))
        
        # enumerate X+1 ways, take min and max element from min_four and max_four
        res = float('inf')
        for i in range(times + 1):
            res = min(
                res,  max_four[i] - min_four[i]
            )
            
        return res

class SolutionC:    
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        diffs = []
        nums.sort()
        
        # 4 possible move ways
        # move 0 left elements, 3 right elements
        diffs.append(nums[-4] - nums[0])
        # move 1 left elements, 2 right elements
        diffs.append(nums[-3] - nums[1])
        # move 2 left elements, 1 right elements
        diffs.append(nums[-2] - nums[2])
        # move 3 left elements, 0 right elements
        diffs.append(nums[-1] - nums[3])
        
        return min(diffs)
    
  
solution = SolutionA()
nums = [0, 1, 1, 1, 6, 6, 6]
ans = solution.minDifference(nums)
print(ans)  # 1

[20,75,81,82,95]