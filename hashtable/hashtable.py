import hashlib

class HashTable(object):

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        index = self.hash(key)
        for d in self.table[index]:
            if d[0] == key:
                d[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for d in self.table[index]:
            if d[0] == key:
                return d[1]
        return None


hash_table = HashTable()
hash_table.add('pc', 'mac')
hash_table.add('sns', 'youtube')
hash_table.add('sns', 'mixi')
print(hash_table.table)
print(hash_table.get('i'))
