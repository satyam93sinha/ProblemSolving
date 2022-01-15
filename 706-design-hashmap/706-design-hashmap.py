class MyHashMap:

    def __init__(self, size=2069):
        self.hashmap = []
        self.size = size
        for _ in range(self.size):
            self.hashmap.append(-1)
    
    def get_index(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.get_index(key)
        if self.hashmap[index] == -1:
            self.hashmap[index] = [[key, value]]
        else:
            self.remove(key)
            self.hashmap[index].append([key, value])

    def get(self, key: int) -> int:
        index = self.get_index(key)
        if self.hashmap[index] != -1:
            for key_, val in self.hashmap[index]:
                if key_ == key:
                    return val
        return -1

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        if self.hashmap[index] == -1:
            return
        else:
            for index_, key_val in enumerate(self.hashmap[index]):
                key_, val = key_val[0], key_val[1]
                if key_ == key:
                    self.hashmap[index].pop(index_)
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)