
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0]*1001
        for trip in trips:
            car[trip[1]] += trip[0];
            car[trip[2]] -= trip[0];
            
        for stop in car:
            capacity -= stop
            if capacity < 0:
                return False;
        return True
