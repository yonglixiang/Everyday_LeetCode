"""
"""
class SolutionA:
    def bestClosingTime(customers: str) -> int:
        count = 1
        customersArr = [0] * (len(customers) + 1) # customerArr[0] = 0
        valueArr = [0] * (len(customers) + 1) # valueArr[0] = 0, which means the value = 0 if never open the shop
        
        # transfer str to [], y = 1 \ n = -1, which means if the shop is open at this time, if customers come value +1\ else value - 1
        while count <= len(customers):
            if customers[count - 1] == "Y":
                customersArr[count] = 1
            else:
                customersArr[count] = -1
            count += 1
        
        # Use dynamic plan to calculate each time's openning value value[count] = value[count-1] + whether customer come today(1 / -1)
        count = 1 
        while count < len(customersArr):
            valueArr[count] = valueArr[count - 1] + customersArr[count]
            count += 1      
        return valueArr.index(max(valueArr))
              
    
class SolutionB:
    def bestClosingTime(customers: str) -> int:
        # if today the shop is openning, how many value will get today. If customers comes, openvalue + 1, else openvalue - 1
        def openValue(customers: str, n: int):
            if n == 0: 
                return 0
            elif customers[n - 1] == "Y":
                return 1
            else:
                return -1
        openValues = [0] * (len(customers) + 1) # valueArr[0] = 0, which means the value = 0 if never open the shop
        
        # Use dynamic plan to calculate each time's openning value value[count] = value[count-1] + whether customer come today(1 / -1)
        count = 1 
        while count <= len(customers):
            openValues[count] = openValues[count - 1] + openValue(customers, count)
            count += 1      
        return openValues.index(max(openValues))