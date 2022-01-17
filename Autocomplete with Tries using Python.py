# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
class TrieNode:
    def __init__(self):
        self.is_word=False
        self.children={}

    def insert(self , char):
        if char not in self.children:
            self.children[char]=TrieNode()
        else:
            pass

    def suffixes(self , suffix=''):
        result=[]

        if suffix!='' and self.is_word:
            result.append(suffix)

        if len(self.children)==0:
            return result

        result=[]

        if suffix!='' and self.is_word:
            result.append(suffix)

        for char in self.children:
            result.extend(self.children[char].suffixes(suffix+char))

        return result

class Trie(object):
    def __init__(self):
        self.root=TrieNode()

    def insert(self , word):
        node=self.root
        for char in word:
            node.insert(char)
            node=node.children[char]
        node.is_word=True

    def find(self , word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]

        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('an')



#IF ON JUPYTER NOTEBOOK UNCOMMENT THE CODE BELOW:
# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');
