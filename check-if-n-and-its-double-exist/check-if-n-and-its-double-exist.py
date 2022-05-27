class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            if hashmap.get(num/2, False) or hashmap.get(num*2, False):
                return True
            hashmap[num] = hashmap.get(num, 0) + 1
        
        return False