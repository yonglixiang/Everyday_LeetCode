'''
The key of this question:
1. we should assign bigger value for the city which has more roads.
2. the total importance can be calculate by city_value and city_road_amount
    - total importance = for each road, city_value_a + city_value_b
    -> total importance = for each city, city_value * city_road_amount
'''
class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        # Calculate the amount of roads for each city
        city_roads_ammounts = [0] * n
        for city_a, city_b in roads:
            city_roads_ammounts[city_a] += 1
            city_roads_ammounts[city_b] += 1
        
        # Assign value from 1 to n, with the ascesing order of roads amount
        city_roads_ammounts.sort()
        
        # Calculate the total importance of the road
        # total importance = sum(city_roads_amount * city_value)
        total = 0
        city_value = 1
        for city_road in city_roads_ammounts:
            total += city_road *  city_value
            city_value += 1
            
        return total

n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
solution = Solution()
map = solution.maximumImportance(n, roads)
print(map)  # 43

            
                    
                    
        
        