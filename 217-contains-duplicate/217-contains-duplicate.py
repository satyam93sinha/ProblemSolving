"""
Edge Cases:
1. No element appears twice; return False
2. More than one element appears twice; return True
3. At most one element appears twice; find that element and return it.

Approaches:
1. Brute Force, Use Hashing
Time: O(n)
Space: O(n) for hashmap/set to store the elements of nums array where we will check if it has already been seen or not.
Intuition:
Iterate over the nums array to check if we have already seen the current iterating number or not. If seen, return the number else add the number to the set.

2. Optimised, Use Xor operation/Bitmasking
Can only be used when we have single element appearing twice!!
Time: O(n)
Space: O(1)
Intuition:
xor operation of 0 ^ 1 gives 1, two different digits give 1.

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)