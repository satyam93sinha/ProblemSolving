"""
Edge Cases:
1. nums array is already sorted
2. Normal Case -> nums array is not sorted

Approaches:
1. Brute Force
Time: O(nlogn) to sort the whole array
Space: O(1) we can use inbuilt sort method to sort or randomised quick sort
Simply sort the array and return it.

2. In Two Passes -> There are just three distinct integers so we can count the number of their occurrences and store in two/three different variables and replace nums array's values to get the answer
Time: O(n)
Space: O(1)

3. In Single Pass, no extra space used -> Keep track of zero and two nums, 0s will be at the begining of the nums array whereas 2s towards the end. So, we can iterate over the nums array indices and:
a. Send 0s to the beginning of nums array
How? -> swap(nums[curr], nums[zero]) and increment curr and zero pointers if nums[curr] == 0.
Why increment zero? -> so that the next time when we encounter 0 we can place it towards the beginning of the nums array. 
Why increment curr? -> we have already changed and got the min element so let's find the next element.
b. Send 2s to the end of the nums array: How? -> swap(nums[curr], nums[two]) and decrement two pointer if nums[two] == 2.
Why decrement two? -> so that next time when we encounter 2, it can be placed at its correct position from end.
Why not increment curr? -> We can come across a situation where the number swapped is 2 again so nums[curr] == 2 and we need to send it back towards the end thus, we DON'T INCREMENT curr pointer here.
c. else when nums[curr] == 1, we simply increment curr pointer
Time: O(n)
Space: O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # Approach1
        # nums.sort()
        # return nums
        """
        """
        # Approach2
        zero_count, one_count, two_count = 0, 0, 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
        
        for index in range(len(nums)):
            if zero_count:
                nums[index] = 0
                zero_count -= 1
            elif one_count:
                nums[index] = 1
                one_count -= 1
            else:
                nums[index] = 2
                two_count -= 1
        """
        # Approach3
        zero_pointer, two_pointer = 0, len(nums)-1
        curr = 0
        while curr <= two_pointer:
            if nums[curr] == 0:
                # send 0s to the beginning of the array
                nums[curr], nums[zero_pointer] = nums[zero_pointer], nums[curr]
                zero_pointer += 1
                curr += 1
            elif nums[curr] == 2:
                # send 2s to the end of the array
                nums[curr], nums[two_pointer] = nums[two_pointer], nums[curr]
                two_pointer -= 1
            else:
                curr += 1