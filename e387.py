'''
The key of this question:
1. try to understand the Counter use, or we can complete dictionary by ourselves
2. when write loop, try to use the loop that has less times:
    In this case, we could use either "for char in s" or "for char,times in dict"
    - The previous ones loop times is determined by the length of s, up to ...
    - The previous ones loop times is determined by the length of dict, up to 26, usually less than first one.
'''
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = Counter(s)
        # dictionary = {}
        # for char in s:
        #     dictionary.setdefault(char, 0)
        #     dictionary[char] += 1
        
        for char, times in dictionary.items():
            if times == 1:
                return s.index(char)
        
        return -1

s = "loveleetcode"
solution = Solution()
print(solution.firstUniqChar(s))  # 2