import pytest
from ..Model.WordStatistics import WordStatistics
from ..Model import WordDict
from ..Model.Config import config
from pathlib import Path
import os
import pickle

STATISTICSFILEPATH = "statisticsfilepathtest"
ws = WordStatistics.WordStatistics('TEST')
text_test = "Hi! My name is (what?), my name is (who?), my name is Slim Shady"
list_text_test = ["hi", "my", "name", "is", "what", "my", "name", "is", "who", "my", "name", "is", "slim", "shady"]
ws.insertText(text_test)
config_env = config['TEST']

@pytest.mark.run(order=1)
def test_insert_words_to_wordstatistics_vs_WordDict():
    wd = WordDict.WordDict()
    wd.insertList(list_text_test)
    assert ws.main_word_dict == wd

@pytest.mark.run(order=2)
def test_number_of_MY_need_to_set_3():
    assert ws.getWordCounter("my") == 3

@pytest.mark.run(order=3)
def test_persistant_is_working():
    file_path = config_env[STATISTICSFILEPATH]
    full_persistent_file_path = (Path(__file__).parent.parent).joinpath(file_path)
    with open(full_persistent_file_path, 'rb+') as open_file:
        tr = pickle.load(open_file)
    assert tr == ws.main_word_dict


@pytest.mark.run('last')
def test_delete_files():
        file_path = config_env[STATISTICSFILEPATH]
        full_persistent_file_path = (Path(__file__).parent.parent).joinpath(file_path)
        os.remove(full_persistent_file_path)


