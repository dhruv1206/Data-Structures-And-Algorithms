'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
class TrieNode(object):
    def __init__(self):
        self.is_word=False
        self.children={}

class Trie(object):
    def __init__(self):
        self.root=TrieNode()

    def add(self , word):
        node=self.root

        for char in word:
            if char in node.children:
                node=node.children[char]
            else:
                node.children[char]=TrieNode()
                node=node.children[char]

        node.is_word=True
                
    def exists(self , word):
        node=self.root

        for i,char in enumerate(word):
            if i==len(word)-1:
                try:
                    node=node.children[char]
                    return node.is_word
                except KeyError:
                    return False

            else:
                try:
                    node=node.children[char]
                except KeyError:
                    return False

word_list = ['Instagram', 'Facebook', 'Whatsapp', 'LinkedIn', 'Twitter']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['FB', 'Facebook', 'Inst', 'Instagram']


for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
