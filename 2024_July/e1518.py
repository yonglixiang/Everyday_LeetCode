'''
1518. Water Bottles
Easy

Question:
    There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Example:
    Input: numBottles = 9, numExchange = 3
    Output: 13
    Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
    Number of water bottles you can drink: 9 + 3 + 1 = 13.
    
Solution:
    1. At first, drink all bottles of water, initial the value of the drink,empty, water with numBottles
    2. for each turn
        - firstly, use the empty bottle to exchange the water bottle, update water_bottle and empty_bottle
        - secondly, drink the water, update drink_bottle and empty_bottle
    3. finished when the empty_bottle < numExchange, because we can not exchange water anymore
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # the first drink
        drink_bottles = numBottles
        empty_bottles = numBottles
        water_bottles = numBottles
        
        while empty_bottles >= numExchange:
            # exchange
            water_bottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
            
            # drink
            drink_bottles += water_bottles
            empty_bottles += water_bottles
            
        return drink_bottles


s = Solution()
numBottles = 15
numExchange = 4
print(s.numWaterBottles(numBottles, numExchange))  # 19