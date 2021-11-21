'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

import functools

@functools.lru_cache(maxsize=None)

class HashTable(object):
	def __init__(self):
		self.table=[None]*10000

	def store(self , string):
		key=self.calculate_hash_value(string)
		if self.table[key] is not None:
			self.table[key].append(string)
		else:
			self.table[key]=[string]

	def lookup(self ,string):
		key=self.calculate_hash_value(string)
		if self.table[key]:
			if string in self.table[key]:
				return key
		return -1

	def calculate_hash_value(self , string):
		return ord(string[0])*100+ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
