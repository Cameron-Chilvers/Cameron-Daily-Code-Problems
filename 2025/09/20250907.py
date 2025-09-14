# Success, created trie, had trouble with the prefix but got it in the end


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

import unittest

class TrieNode:
    def __init__(self):
        self.children:list[TrieNode] = [None]*26
        self.end_of_word = False
    
    def get_node_at(self, i):
        return self.children[i]
    
    def set_node_at(self, i, node):
        self.children[i] = node
    
    def get_end_of_word(self):
        return self.end_of_word
    
    def set_end_of_word(self, val):
        self.end_of_word = val

    def get_all_children(self):
        return [child for child in self.children]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert class
    def insert(self, word:str):
        curr_node = self.root
        word = word.lower()
        for c in word:
            i = ord(c)-97
            if curr_node.get_node_at(i) is None: # if doesn't exist then create a node
                curr_node.set_node_at(i, TrieNode())
            curr_node = curr_node.get_node_at(i)

        curr_node.set_end_of_word(True)

    # Search
    def search(self, word:str) -> bool:
        if len(word) == 0:
            return False

        curr_node = self.root
        word = word.lower()
        for c in word: # go to bottom of prefix and then get all nodes
            i = ord(c)-97
            if curr_node is None:
                return False

            curr_node = curr_node.get_node_at(i)

        return True if curr_node is not None else False
    
    # Prefix search
    def prefix_search(self, prefix:str):
        curr_node = self.root
        prefix = prefix.lower()

        for c in prefix: # go to bottom of prefix and then get all nodes
            i = ord(c)-97
            if curr_node is None:
                return []

            curr_node = curr_node.get_node_at(i)
        if curr_node is None: # check to see if node is in the trie
            return []

        nodes = curr_node.get_all_children() # get all nodes

        def get_words(nodes_traverse:list[TrieNode], res:list, prefix:str): 
            for i, node in enumerate(nodes_traverse):
                if node is None: # skip if no char
                    continue

                cur_word = prefix + chr(i+97) # append char to prefix
                if node.get_end_of_word(): # check if finished word
                    res.append(cur_word) # add for to completed

                get_words(node.get_all_children(), res, cur_word)# get all next nodes and traverse down

            return res

        res = get_words(nodes, [], prefix) # loop all nodes
        return res


def get_prefix(prefix:str, words:list[str]):
    trie = Trie()

    for word in words:
        trie.insert(word.lower())

    res = trie.prefix_search(prefix)

    return res

def search(search_word:str, words:list[str]):
    trie = Trie()

    for word in words:
        trie.insert(word.lower())

    return trie.search(search_word)

class Test_Problem(unittest.TestCase):
    def test_prefix(self):
        self.assertEqual(get_prefix('de', ['dog', 'deer', 'deal']), ['deal', 'deer'])
        self.assertEqual(get_prefix('de', ['dog', 'deer', 'deal', 'deals', 'destroy', 'dogs']), sorted(['deer', 'deal', 'deals', 'destroy']))
        self.assertEqual(get_prefix('do', ['dog', 'deer', 'deal', 'deals', 'destroy', 'dogs']), sorted(['dog', 'dogs']))

        self.assertEqual(get_prefix('', ['apple', 'banana', 'apricot']), sorted(['apple', 'apricot', 'banana']))  
        self.assertEqual(get_prefix('a', ['apple', 'banana', 'apricot']), sorted(['apple', 'apricot']))       
        self.assertEqual(get_prefix('ap', ['apple', 'apricot', 'banana', 'ape']), sorted(['apple', 'apricot', 'ape'])) 
        self.assertEqual(get_prefix('z', ['apple', 'banana', 'apricot']), [])                                  
        self.assertEqual(get_prefix('ban', ['banana', 'band', 'bandana', 'apple']), sorted(['banana', 'band', 'bandana']))  
        self.assertEqual(get_prefix('banda', ['banana', 'band', 'bandana', 'apple']), ['bandana'])             

    def test_search(self):
        self.assertEqual(search('dog', ['dog', 'deer', 'deal']), True)
        self.assertEqual(search('duck', ['dog', 'deer', 'deal']), False)
        self.assertEqual(search('do', ['dog', 'deer', 'deal', 'deals', 'destroy', 'dogs']), True)
        self.assertEqual(search('destroy', ['dog', 'deer', 'deal', 'deals', 'destroy', 'dogs']), True)

        self.assertEqual(search('', ['apple', 'banana', 'apricot']), False)   
        self.assertEqual(search('Apple', ['apple', 'banana', 'apricot']), True) 
        self.assertEqual(search('band', ['banana', 'band', 'bandana']), True)
        self.assertEqual(search('bandana', ['banana', 'band', 'bandana']), True)
        self.assertEqual(search('bandanas', ['banana', 'band', 'bandana']), False) 

if __name__ == '__main__':


    unittest.main()