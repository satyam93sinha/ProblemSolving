class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                hashset.remove(nums[left])
                left += 1
            if nums[right] in hashset and abs(right-left) <= k:
                return True
            hashset.add(nums[right])
        
        return False