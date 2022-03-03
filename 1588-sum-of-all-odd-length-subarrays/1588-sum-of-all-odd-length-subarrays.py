class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = sum(arr)
        
        for index in range(len(arr)):
            for index2 in range(index+1, len(arr)):
                if (index2-index+1) % 2 == 1:
                    total_sum += sum(arr[index:index2+1])
        
        return total_sum
        