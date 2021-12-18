from collections import Counter
'''
Edge Cases:
1. all numbers are distinct, return any k elements
2. k == N, return whole array provided 1 <= k <= N and k will be equal to N iff array has n distinct elements
3. normal case

{1: 3, 2: 2, 3: 1, 4: 5}, k = 2
[2, 1, 3, 4]

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the number and its corresponding frequency
        num_frequency = Counter(nums)
        # set of numbers we have to consider
        nums = list(set(nums))
        return self.quick_divide(nums, 0, len(nums)-1, len(nums)-k, num_frequency)
    
    def quick_divide(self, nums, start, end, k, num_frequency):
        if start > end:
            return
        partition_index = self.partition(nums, start, end, num_frequency)
        if partition_index == k:
            return nums[k:]
        elif partition_index > k:
            return self.quick_divide(nums, start, partition_index - 1, k, num_frequency)
        else:
            return self.quick_divide(nums, partition_index + 1, end, k, num_frequency)
    
    def partition(self, nums, start, end, num_frequency):
        random_index = random.randint(start, end)
        nums[random_index], nums[end] = nums[end], nums[random_index]
        # randomisation of pivot is done, select it as pivot
        pivot = nums[end]
        # keep track of correct position of pivot index
        pivot_index = start
        
        while start < end:
            if num_frequency[nums[start]] <= num_frequency[pivot]:
                nums[pivot_index], nums[start] = nums[start], nums[pivot_index]
                pivot_index += 1
            start += 1
        
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
        return pivot_index
                
                
        