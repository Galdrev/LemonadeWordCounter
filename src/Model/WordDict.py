class WordDict():

    def __init__(self):
        self.word_dict = dict()

    def __eq__(self, other):
        for key, value in self.word_dict.items():
            if other.word_dict.get(key, -1) != value:
                return False
        return True

    def search(self, word):
        return self.word_dict.get(word, 0)

    def __addSingleInstanse(self, word):
        if word not in self.word_dict:
            self.word_dict.setdefault(word, 1)
        else:
            self.word_dict[word] = self.word_dict[word]+1

    def insertList(self, words):
        for word in words:
            input_word = word.lower()
            self.__addSingleInstanse(input_word)





