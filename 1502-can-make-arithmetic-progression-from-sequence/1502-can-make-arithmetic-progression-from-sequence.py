class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_num = min(arr)
        common_difference = (max(arr) - min_num)//(len(arr)-1)
        arr_set = set(arr)  # O(n) time and space to convert list to set
        for _ in range(len(arr)):
            if min_num in arr_set:
                min_num += common_difference
            else:
                return False
        return True