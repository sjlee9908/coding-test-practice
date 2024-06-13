class MyHashMap:
    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        x = self.hashmap.get(key)
        if x == None:
            return -1
        else:
            return x

    def remove(self, key: int) -> None:
        if key not in self.hashmap.keys():
            return -1
        else:
            self.hashmap.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)