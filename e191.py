class SolutionA:
    def hammingWeight(self, n: int) -> int:
        num = int(n)
        cal = 0
        while num > 0:
            if num % 2 == 1:
                cal += 1
            num = num // 2
        return cal
    
class SolutionB:
    def hammingWeight(self, n: int) -> int:
        num = int(n)
        cal = 0
        while num > 0:
            cal += num & 1
            num >>= 1
        return cal
       