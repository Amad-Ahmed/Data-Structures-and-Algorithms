class MyHashSet:

    def __init__(self):
        self.bucket = []

    def add(self, key: int) -> None:
        i = 0
        while i < len(self.bucket):
            if (self.bucket[i] == key):
                break
        self.bucket.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.bucket):
            if (self.bucket[i] == key):
                self.bucket.remove(key)
                break

    def contains(self, key: int) -> bool:
        i = 0
        while i < len(self.bucket):
            if (self.bucket[i] == key):
                return True
        return False


# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
