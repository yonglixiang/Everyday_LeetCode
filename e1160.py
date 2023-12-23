class SolutionA:
    def countCharacters(words:[str], chars: str) -> int:
        import copy
        #calulate the valuable times for each character
        charCounts = [0] * 26
        i = 0
        while i < len(chars):
            charCounts[ord(chars[i]) - ord('a')] += 1
            i += 1
        
           
        cal = 0
        i = 0
        while i < len(words):
            subCharCounts = copy.copy(charCounts)
            j = 0
            while j < len(words[i]):
                # this character is uesd once,so decrease the avaliable time
                subCharCounts[ord(words[i][j]) - ord('a')] -= 1  
                j += 1
            # if there are some character left or = 0, the word can be performed
            if min(subCharCounts) >= 0: 
                cal += len(words[i])
            i += 1
        return cal

class SolutionB:
    def countCharacters(words: [str], chars: str) -> int:
        import copy
        #calulate the valuable times for each character 
        charCounts = [0] * 26
        i = 0
        while i < len(chars):
            charCounts[ord(chars[i]) - ord('a')] += 1
            i += 1
        
           
        cal = 0
        i = 0
        while i < len(words):
            subCharCounts = copy.copy(charCounts)
            j = 0
            while j < len(words[i]):
                # this characater is not avaliable, so this str cannot perform this word
                if subCharCounts[ord(words[i][j]) - ord('a')] == 0:
                    break
                else:
                    subCharCounts[ord(words[i][j]) - ord('a')] -= 1
                    j += 1
            # if j == len, the forming processes have spelt the whole word, which means this word can be performed
            if j == len(words[i]):
                cal += j
            i += 1
        return cal

class SolutionC:
    def countCharacters(words: [str], chars: str) -> int:
        #calulate the valuable times for each character 
        charCounts = [0] * 26
        charLength = len(chars)
        aCode = ord('a')
        for char in chars:
            charCounts[ord(char) - aCode] += 1
        
           
        cal = 0
        for word in words:
            if len(word) > charLength:
                continue
            times = [0] * 26
            count = 0
            for char in word:
                code = ord(char) - aCode 
                if (charCounts[code] - times[code]) == 0: # this characater is not avaliable, so this str cannot perform this word
                    cal -= count
                    break
                times[code] += 1 # record the using time of characters for each word
                cal += 1
                count += 1
        return cal


    
SolutionC.countCharacters(["hello","world","leetcode"],"welldonehoneyr")