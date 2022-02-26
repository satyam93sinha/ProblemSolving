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
        # high - low gives us the total count of odd numbers 0-indexed,
        # to get the length, we need to increment it by 1
        # example: 7 - 3 = 4//2 = 2 => 3, 5, 7 ==> 2 + 1 = 3
        # example: 9 - 9 = 0//2 = 0 => 9 ==> 0 + 1 = 1
        # example: 101 - 33 = 68//2 = 34 ==> 34 + 1 = 35
        return (high - low) // 2 + 1