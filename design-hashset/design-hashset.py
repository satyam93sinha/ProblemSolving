class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(2069)]
        self.size = 2069

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        hash_key = key % self.size
        self.hashset[hash_key].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        hash_key = key % self.size
        self.hashset[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = key % 2069
        for num_key in self.hashset[hash_key]:
            if num_key == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)