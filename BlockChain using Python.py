'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

import time 
import hashlib


class Block:
    def __init__(self , data , previous_hash=None):
        self.previous_hash=previous_hash
        self.data=data
        self.hash=self._calc_hash(data)
        self.timestamp=time.time()

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

    def _calc_hash(self , string: str) -> str:
        """
        Given a string, calculates the SHA-256 hash of it
        :param string: text we want to calculate th hash of
        :return: hash of the imputed text
        """
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail=None

    def append(self , data):
        if self.tail is None:
            self.tail=Block(data)
        else:
            self.tail=Block(data , self.tail)

    def search(self , data):
        if self.tail is None:
            print("Please 'append' data on the BlockChain before searching for it")
            return 

        while self.tail:
            if self.tail.data==data:
                return self.tail
            self.tail=self.tail.previous_hash

        return None

    def size(self):
        temp=self.tail
        lenght=0

        while temp:
            temp=temp.previous_hash
            lenght+=1

        return lenght

    def to_list(self):
        out=[]
        temp=self.tail

        while temp:
            out.append([temp.data , temp.timestamp , temp.hash])
            temp=temp.previous_hash

        return out

#%% Testing official
blockchain = BlockChain()

print(blockchain.size())
# 0
print(blockchain.to_list())
# []

blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')
print(blockchain.size())
# 1
print(blockchain.to_list())
# [['my balance: 0 | cash flow: +10 | final balance: 10', 1564306421.0008988, '5e5a93abe59f9e92b38e00ebc7a50c50f902f5a8
# 210d327590a36ffb25a831d9']]

blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
print(blockchain.size())
# 5
print(blockchain.to_list())
# [['my balance: 145 | cash flow: +5 | final balance: 150', 1564306378.6235423, '43841086a72ab23dacc07ac04341357ed73
# 51a07f8c8f0df92056cd439f49302'], ['my balance: 20 | cash flow: +125 | final balance: 145', 1564306378.6235056, '597f
# 549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e'], ['my balance: 35 | cash flow: -15 | final balance: 20'
# , 1564306378.623468, '6da8edd2d3d03bfa69810f7390ce55a64bab5102b79e37c973a4bed4be303e77'], ['my balance: 10 |
# cash flow: +25 | final balance: 35', 1564306378.6234293, 'ed240a001a354b3ee5f36db5ccdbcac1235806a106907feaedd9db02c
# 6ee7dfc'], ['my balance: 0 | cash flow: +10 | final balance: 10', 1564306378.6233213, '5e5a93abe59f9e92b38e00ebc7a50
# c50f902f5a8210d327590a36ffb25a831d9']]

# Testing the "search function"
print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
# Block is:
# Data: my balance: 20 | cash flow: +125 | final balance: 145
# Timestamp: 1564305924.884146
# Hash: 597f549af039dbb1c79d5e4ae5c347189cf7b8bafc12011f44b0cc06692ade9e


# Edge Cases:
print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))
# None

blockchain = BlockChain()
print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
# Please 'append' data on the BlockChain before searching for it
