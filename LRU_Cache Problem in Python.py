'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self , capacity):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self , key):
        try:
            value=self.cache.pop(key)
            self.cache[key]=value
            return value
        except: 
            return -1
    def set(self , key , value):
        if self.capacity<=0:
            print("Can't perform operation on 0 capacity!")
            return

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key]=value 
        else:
            if len(self.cache)<(self.capacity):
                self.cache[key]=value

            else:
                self.cache.popitem(last=False)
                self.cache[key]=value

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1
