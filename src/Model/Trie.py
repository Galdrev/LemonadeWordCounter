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
            self.root.insert(input_word)

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

        def insert(self, word):
            assert (word.islower())
            assert (word.isalpha())
            return self.insertRec(word, 0)

        def insertRec(self, word, index):
            if index >= len(word):
                self.is_word = True
                self.counter += 1
                return

            if word[index] not in self.children:
                self.children[word[index]] = Trie.TrieNode()
            return self.children[word[index]].insertRec(word, index+1)

        def search(self, word, index=-1):
            if (index == len(word)-1):
                return self.counter
            next_child = self.children.get(word[index+1], None)
            return next_child.search(word, index+1) if next_child else 0