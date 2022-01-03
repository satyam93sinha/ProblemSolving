"""
Intuition: Maintain a candidate and check if that candidate is the one in consideration, if so we increment the count of that candidate being seen as +1 else -1. If the count reaches 0 we can forget about the candidate in consideration and choose current candidate
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate
        