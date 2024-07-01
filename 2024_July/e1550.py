class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        '''
        Given an integer array arr, return true if there are three consecutive odd numbers in the array. 
        Otherwise, return false.
        '''
        count = 0 
        for num in arr:
            if num % 2 == 1:
                count += 1
            else:
                count = 0
            
            if count == 3:
                return True
        
        return False

solution = Solution()
arr = [1,2,34,3,4,5,7,23,12]
arr = [2,6,4,1]
answer = solution.threeConsecutiveOdds(arr)
print(answer) # true