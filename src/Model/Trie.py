from src.Model.Constants import *


class Trie():

    def __init__(self, words=""):
        self.root = self.TrieNode()
        self.insertList(words)

    def __eq__(self, other):
        return self.root == other.root

    def insertList(self, words):
        for word in words:
            input_word = word.lower()
            self.insert(input_word)

    def insert(self, word):
        assert (word.islower())
        assert (word.isalpha())
        return self.insertRec(self.root, word, 0)

    def insertRec(self, node, word, index):
        if index >= len(word):
            node.is_word = True
            node.counter += 1
            return

        if word[index] not in node.children:
            node.children[word[index]] = Trie.TrieNode()
        return self.insertRec(node.children[word[index]], word, index + 1)

    def search(self, word, index=-1):
        return self.searchRec(self.root, word, index)

    def searchRec(self, node, word, index):
        if (index == len(word) - 1):
            return node.counter
        next_child = node.children.get(word[index + 1], None)
        return self.searchRec(next_child, word, index + 1) if next_child else 0

    class TrieNode():
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.children = dict()
            self.counter = 0

        def __eq__(self, other):
            if self.is_word != other.is_word:
                return False
            for key, child in self.children.items():
                if key not in other.children:
                    return False
                if (self.children[key] != other.children[key]):
                    return False
            return True



