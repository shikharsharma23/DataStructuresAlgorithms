from LinkedList import *

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 4
        self.buckets = [None]*15000


    def hash_function(self, key):
        return key%self.num_buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        bucket_to_map = self.hash_function(key);
        if self.buckets[bucket_to_map] is None:
            self.buckets[bucket_to_map] = LinkedList()
            self.buckets[bucket_to_map].head = Node((key, value))
        else:
            current_data = self.buckets[bucket_to_map].head
            while current_data:
                if key == current_data.data[0]:
                    current_data.data = (key, value)
                    return
                current_data = current_data.next

            self.buckets[bucket_to_map].insertion_at_beginning((key, value))



    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_to_map = self.hash_function(key);
        if self.buckets[bucket_to_map] is None:
            return -1
        bucket_data = self.buckets[bucket_to_map].head
        while bucket_data:
            if bucket_data.data[0] == key:
                return bucket_data.data[1]
            bucket_data = bucket_data.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_to_map = self.hash_function(key);
        if self.buckets[bucket_to_map] is None:
            return
        else:
            value = self.get(key)
            self.buckets[bucket_to_map].remove_item((key,value))




# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,5)
obj.put(13,6)
obj.put(4,9)
obj.put(4,8)
obj.put(13,9)
obj.put(5,9)

print(obj.get(1))
print(obj.get(13))
print(obj.get(4))
print(obj.get(80))

obj.remove(13)
obj.remove(4)

print(obj.get(13))
print(obj.get(4))

