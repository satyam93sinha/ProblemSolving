class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        
        while start < end:
            current_sum = numbers[start] + numbers[end]
            if current_sum > target:
                end -= 1
            elif current_sum < target:
                start += 1
            else:
                return [start+1, end+1]
        
        