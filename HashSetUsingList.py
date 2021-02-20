## for leetcode problem 705
class MyHashSet:

    def __init__(self):
        self.buckets = 150000
        self.hashset = [[] for _ in range(self.buckets)]

    def hash_function(self, key):
        target_index = key % self.buckets
        return target_index

    def add(self, key: int) -> None:
        if key not in self.hashset[self.hash_function(key)]:
            self.hashset[self.hash_function(key)].append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset[self.hash_function(key)]:
            self.hashset[self.hash_function(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset[self.hash_function(key)]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)