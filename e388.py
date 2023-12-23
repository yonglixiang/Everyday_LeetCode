""""""
class SolutionA:
    def countBits(n: int):
        num = 0
        arr = [0] * (n + 1)
        while num <= n:
            eachNum = num
            cal = 0
            while eachNum > 0:
                cal += eachNum % 2
                eachNum //= 2
            arr[num] = cal
            num += 1
        return arr



class SolutionB:
    def countBits(n: int):
        num = 1
        arr = [0] * (n + 1)
        while num <= n:
            arr[num] = arr[num >> 1] + (num & 1)
            num += 1
        return arr
            