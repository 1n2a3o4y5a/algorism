import hashlib

class HashTable(object):

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        index = self.hash(key)
        self.table[index].append([key, value])


hash_table = HashTable()
hash_table.add('pc', 'mac')
