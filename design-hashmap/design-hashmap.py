class MyHashMap:

    def __init__(self):
        self.hashmap = [[] for _ in range(2069)]
        self.size = 2069

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        for index, key_val in enumerate(self.hashmap[hash_key]):
            if key_val[0] == key:
                self.hashmap[hash_key][index][1] = value
                return
        self.hashmap[hash_key].append([key, value])

    def get(self, key: int) -> int:
        hash_key = key % self.size
        for num_key, num_val in self.hashmap[hash_key]:
            if num_key == key:
                return num_val
        return -1

    def remove(self, key: int) -> None:
        num_val = self.get(key)
        if num_val == -1:
            return
        hash_key = key % self.size
        self.hashmap[hash_key].remove([key, num_val])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)