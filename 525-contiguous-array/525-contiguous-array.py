"""
Deduction:
1. Array is binary containing only 0s and 1s. 
2. To find -> longest contiguous length of an equal number of 0s and 1s. 
3. All the 0s and 1s should be contiguous and together. 
4. 0s and 1s could be in any order.

Edge Cases:
1. Contains only single element; return 0
2. Contains only two elements; single 0 and single 1; return 2
3. First half of array contains 0s/1s and second half contains 1s/0s.
4. Contains multiple combinations of 0s and 1s together; find longest contiguous length of equal number of 0s and 1s. (Normal Case)


Test Cases:
1. [0] or [1]
2. [0, 1] or [1, 0]
3. [0, 0, 0, 1, 1, 1] or [1, 1, 1, 0, 0, 0]
4. [0, 1, 1, 0, 0, 0, 1, 1, 1]

Approaches:
1. Brute Force

"""
class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length