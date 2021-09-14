from src.Model.WordStatistics import WordStatistics
import urllib.request
from src.Model.Constants import *

class InputHandler():

    word_stat = None
    def __init__(self, context_config):
        self.word_stat = WordStatistics.WordStatistics(context_config)

    def fileHandler(self, file_path):
        try:
            with open(file_path, 'r+') as input_file:
                for line in input_file:
                    line = line.rstrip('\n')
                    self.__insertNormalized(line)
            self.word_stat.saveWordsStatistics()
        except Exception:
            return False
        return True

    def uriHandler(self, uri):
        try:

            data_url = urllib.request.urlopen(uri)
            for line in data_url:
                decoded_line = line.decode(DECODE_TYPE).rstrip('\n')
                self.__insertNormalized(decoded_line)
            self.word_stat.saveWordsStatistics()
            return True
        except Exception:
            return False

    def textHandler(self, text):
        try:
            self.__insertNormalized(text)
            self.word_stat.saveWordsStatistics()
        except Exception:
            return False
        return True


    def __insertNormalized(self, data):
        try:
            self.word_stat.insertText(data)
        except Exception:
            return False
        return True

    def wordCount(self, word):
        if not word.isalpha():
            return -1
        word = word.lower()
        try:
            word_counter = self.word_stat.getWordCounter(word)
        except Exception:
            return -1
        res = {WORD_STRING: word, COUNTER_STRING: word_counter}
        return res
