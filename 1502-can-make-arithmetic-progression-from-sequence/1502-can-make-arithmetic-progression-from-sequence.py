class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        common_difference = arr[1] - arr[0]
        for index in range(2, len(arr)):
            if arr[index] - arr[index-1] == common_difference:
                continue
            else:
                return False
        return True