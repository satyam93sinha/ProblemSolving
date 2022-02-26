class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count_odd = 0
        # get first lowest odd number
        if low % 2 == 1:
            low = low
        else:
            low = low + 1
        
        # get first highest odd number
        if high % 2 == 1:
            high = high
        else:
            high = high - 1
        
        return (high - low) // 2 + 1