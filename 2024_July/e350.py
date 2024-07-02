'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

SolutionA: use double loop, for each num in nums1, find if there's element in nums2 that is equal to num.
SolutionB: use other 2 temp list as stack, for each element in nums1 and nums2, check if it is in another list.
SolutionC: use dictionary to record nums' counts for nums1/nums2, then check the intersection.
'''

class SolutionA:  # Time Complex: O(n^2)
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    intersection.append(nums1[i])
                    nums1[i] = None
                    nums2[j] = None
                    break
        
        return intersection

class SolutionB:  # Time Complex: O(n^2)
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        temp1 = []
        temp2 = []
        
        while nums1 != [] or nums2 != []:
            if nums1 != []:
                num1 = nums1.pop()
                if num1 in temp2:
                    intersection.append(num1)
                    temp2.remove(num1)
                else:
                    temp1.append(num1)
            
            if nums2 != []:
                num2 = nums2.pop()
                if num2 in temp1:
                    intersection.append(num2)
                    temp1.remove(num2)
                else:
                    temp2.append(num2)
            
        return intersection

class SolutionC:  # Time Complex: O(n)
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_counts = {}
        for num in nums1:
            nums1_counts.setdefault(num, 0)
            nums1_counts[num] += 1
            
        intersection = []
        for num in nums2:
            if nums1_counts.get(num, 0):
                intersection.append(num)
                nums1_counts[num] -= 1
        
        return intersection
            

solution = SolutionC()
nums1 = [1,2,2,1]
nums2 = [2,2]

print(solution.intersect(nums1, nums2))  # [4, 9]
            
            