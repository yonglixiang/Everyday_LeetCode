'''
1598. Crawler Log Folder
Easy

Question:
    The Leetcode file system keeps a log each time some user performs a change folder operation.

    The operations are described below:

    "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
    "./" : Remain in the same folder.
    "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
    You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

    The file system starts in the main folder, then the operations in logs are performed.

    Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example:
    Input: logs = ["d1/","d2/","../","d21/","./"]
    Output: 2
    Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Solution: maintain a variable named 'level', start with 0(main). For each operand: 
    ../ : -1(if level != 0)
    ./ : 0
    x/ : +1
'''

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        level = 0
        
        for operation in logs:
            if '../' in operation:
                if level != 0:
                    level -= 1
            elif './' in operation:
                level += 0
            elif '/' in operation:
                level += 1
        
        return level

s = Solution()
logs = ["d1/","d2/","./","d3/","../","d31/"]
print(s.minOperations(logs))  # 3