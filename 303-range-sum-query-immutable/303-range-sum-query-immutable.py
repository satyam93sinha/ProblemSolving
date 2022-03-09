class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.range_sum = [0 for _ in range(len(nums)+1)]
        for index1, num1 in enumerate(self.nums):
            self.range_sum[index1+1] = self.range_sum[index1] + num1
        
    def sumRange(self, left: int, right: int) -> int:
        return self.range_sum[right+1] - self.range_sum[left]
        # return self.range_sum_dict[(left, right)]
        # Brute Force: O(n) for every query, Space: O(1)
        # return sum(self.nums[left: right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)