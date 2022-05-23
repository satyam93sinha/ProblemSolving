class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_counter = collections.Counter(arr)
        for num, count in arr_counter.items():
            if num == 0:
                if arr_counter[num] > 1:
                    return True
            elif num % 2 == 0:
                if arr_counter[num//2] > 0:
                    return True
            else:
                if arr_counter[num*2] > 0:
                    return True
        return False