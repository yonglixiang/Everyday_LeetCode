"""Leetcode 1662
"""
class SolutionA:
    def arrayStringsAreEqual(word1: [str], word2: [str]):
        count = 0
        index1 = ""
        index2 = ""
        while count < len(word1):
            index1 += word1[count]
            count += 1
        count = 0
        while count < len(word2):
            index2 += word2[count]
            count += 1
        if index1 == index2:
            return True
        else:
            return False

"""Use join function"""
class SolutionB:
    def arrayStringsAreEqual(word1: [str], word2: [str]):
        return "".join(word1) == "".join(word2)
        
