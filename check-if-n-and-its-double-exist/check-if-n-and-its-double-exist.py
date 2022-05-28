class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = collections.Counter(arr)
        if hashmap.get(0, 0) > 1:
            return True
        for num, count in hashmap.items():
            if (hashmap.get(num/2, 0) or hashmap.get(num*2, 0)) and num != 0:
                return True
        return False
        hashmap = {}
        for num in arr:
            if hashmap.get(num/2, False) or hashmap.get(num*2, False):
                return True
            hashmap[num] = hashmap.get(num, 0) + 1
        
        return False