"""
What is a triangle?
A triangle is an enclosed figure with three sides provided the sum of its any and all the two sides will be greater than the third one.

Observation:
Thus, we need to keep the sum of any and all the two sides to be greater than the third one. So we need to check for:
    i) side_1 + side_2 > side_3
    ii) side_1 + side_3 > side_2
    iii) side_2 + side_3 > side_1
or deduce side_1 <= side_2 <= side_3 so that,
    i) side_1 + side_2 > side_3 as side_3 will be maximum of the three sides of triangle, we can be sure that the other two conditions specified above will hold true.

Edge Cases:
1. Does not form a triangle; no perimeter; return 0
2. Forms a triangle; return the largest perimeter

Approaches:
1. Brute Force
Intuition:
Find all the group of three arrays computing their perimeters from the given nums array and return the max perimeter.
Time: O(2^n) for computing all the group of three array from the given nums array
Space: O(2^n) for storing all the computed group of three arrays.

2. Sorting
Intuition:
We need to find the three largest numbers which satisfies the definition of a triangle as mentioned above. So, after sorting we can find them towards the end of the nums array but we are not still sure if they satisfy the triangle sides condition so we will also check if side_1 + side_2 > side_3 and until this happens we keep checking/computing. The minute this condition is fulfilled we have found our answer of finding the largest perimeter of the triangle so we can break out of the loop and return perimeter.
Time: O(nlogn)
Space: O(1)
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = 0
        for index in range(len(nums)-1, 1, -1):
            side_3, side_2, side_1 = nums[index], nums[index-1], nums[index-2]
            if side_1 + side_2 > side_3:
                perimeter = side_1 + side_2 + side_3
                break
        
        return perimeter