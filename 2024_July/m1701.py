'''
1701. Average Waiting Time
Medium

Question:
    There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

    arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
    timei is the time needed to prepare the order of the ith customer.
    When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

    Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
    
Example:
    Input: customers = [[5,2],[5,4],[10,3],[20,1]]
    Output: 3.25000
    Explanation:
    1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
    2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
    3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
    4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
    So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.

Solution:
    - Simulate: time complexity -- O(n), space complexity -- O(1)
        - maintain a variable 'serve', this means for each customer, when their order would be served.
        - after finishing the previous one customer
            - if the next customer has arrived, the server time should add the next order time, which means there's no break between 2 order
            - if the next customer has not arrived, the chief would wait for the next order coming, so the serve time should be equal to arrival + time.
'''

class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        serving = customers[0][0]  # the time that serving the cuisine for customer
        waiting = 0
        count = 0
        
        for arrival, cooking in customers:
            # if serving >= arrival:
            #     serving += cooking  # no break between 2 customers
            # else:
            #     serving = arrival + cooking  # waiting for the next customer to arrive and come and to cook
            
            # The formula is equivalent to the if-else code block logically
            serving = max(serving, arrival) + cooking
            
            waiting += serving - arrival
            count += 1
        
        return waiting / count

customers = [[5,2],[5,4],[10,3],[20,1]]
s = Solution()
print(s.averageWaitingTime(customers))  # 3.25