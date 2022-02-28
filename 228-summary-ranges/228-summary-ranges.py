"""
Edge Cases:
1. All the numbers in the array fall in single range; [0, 1, 2, 3]
2. No number in the array falls in any range; [1, 3, 5]
3. Some of the numbers fall in single range while others do not as shown in the example test cases

Approaches:
1. Sliding Window
Intuition:
Iterate over the array mention begin of range in outer while loop and find end in nested for loop until current element is 1 greater than the previous one. If the latter condition fails, we reset the outer loop index or begin to this new element breaking the range and perform same operation.
Time: O(n) iterating over the array only once
Space: O(1) only taking variables
"""

class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        res, i, start = [], 0, 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        return res

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)            