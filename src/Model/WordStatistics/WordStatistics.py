from src.Model import Trie
from src.Model.Config import *
from src.Model.Constants import *
import re
import pickle



class WordStatistics():

    main_trie = Trie.Trie()
    persistent_file_path = None

    def __init__(self, config_context):
        self.persistent_file_path = config[config_context]
        file_path = self.persistent_file_path[STATISTICSFILEPATH]
        full_persistent_file_path = (Path(__file__).parent).joinpath(file_path)


        if (not full_persistent_file_path.exists()):
            open_file = open(full_persistent_file_path, 'wb+')
            pickle.dump(WordStatistics.main_trie, open_file)
            open_file.close()

        try:
            open_file = open(full_persistent_file_path, 'rb+')
            self.main_trie = pickle.load(open_file)
            open_file.close()
        except FileNotFoundError:
            print("File not found. Server will not be load")
            exit()


    def saveWordsStatistics(self):
        file_path = self.persistent_file_path[STATISTICSFILEPATH]
        full_persistent_file_path = (Path(__file__).parent).joinpath(file_path)
        try:
            open_file = open(full_persistent_file_path, 'wb+')
            pickle.dump(self.main_trie, open_file)
            open_file.close()
        except FileNotFoundError:
            print("Server could not save current statistics snapshot")



    def insertText(self, text):
        filtered_text = filter(None, re.split(r'\W|\d', text))
        self.main_trie.insertList(list(filtered_text))




    def getWordCounter(self, word):
        word_counter = self.main_trie.search(word)
        return word_counter


    def empty_statistics(self):
        self.main_trie = Trie.Trie()
        self.saveWordsStatistics()






